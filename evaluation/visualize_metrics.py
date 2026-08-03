import json
import os
import pandas as pd

from global_layer.functions import _write_json_file


def coverage_band_from_max_score(max_score: float) -> str:
	"""Map max similarity score to coverage band."""
	if max_score > 0.75:
		return "full_coverage"
	if 0.60 <= max_score <= 0.75:
		return "partial_coverage"
	return "no_coverage"

#using the embedding coverage ratio
def build_coverage_ratio_table(filepath: str, output_table_path: str | None = None) -> pd.DataFrame:
	"""Read coverage JSON and return a ratio table for full/partial/no coverage.

	Coverage class is derived from the maximum similarity score in each item's top_matches.
	"""
	with open(filepath, "r", encoding="utf-8") as jsonfile:
		data = json.load(jsonfile)

	# Support either a raw list or wrapped payloads with an items key.
	items = data.get("items", []) if isinstance(data, dict) else data
	total = len(items)

	counts = {
		"full_coverage": 0,
		"partial_coverage": 0,
		"no_coverage": 0,
	}

	for item in items:
		matches = item.get("top_matches", []) or []
		max_score = max((float(match.get("similarity_score", 0.0) or 0.0) for match in matches), default=0.0)
		band = coverage_band_from_max_score(max_score)
		counts[band] += 1

	table = pd.DataFrame(
		[
			{
				"coverage_band": band,
				"count": count,
				"ratio": round((count / total), 4) if total else 0.0,
			}
			for band, count in counts.items()
		]
	)

	if output_table_path:
		output_dir = os.path.dirname(output_table_path)
		if output_dir:
			os.makedirs(output_dir, exist_ok=True)
		table.to_csv(output_table_path, index=False)
		print(f"Saved coverage ratio table to: {output_table_path}")

	return table

def build_coverage_llm_ratio_table(filepath: str, output_table_path: str | None = None) -> pd.DataFrame:
	"""Read LLM Judge coverage evaluation JSON and return a ratio table for full/partial/no coverage."""
	with open(filepath, "r", encoding="utf-8") as jsonfile:
		data = json.load(jsonfile)
	
	# Support either a raw list or wrapped payloads with a coverage/items key.
	items = data.get("coverage", []) if isinstance(data, dict) else data
	total = len(items)

	counts = {
		"full_coverage": 0,
		"partial_coverage": 0,
		"no_coverage": 0,
	}

	for item in items:
		verdict = str(item.get("coverage_verdict", "")).upper()
		if verdict == "FULL":
			counts["full_coverage"] += 1
		elif verdict == "PARTIAL":
			counts["partial_coverage"] += 1
		elif verdict in ("NONE", "NO"):
			counts["no_coverage"] += 1

	table = pd.DataFrame(
		[
			{
				"coverage_verdict": band,
				"count": count,
				"ratio": round((count / total), 4) if total else 0.0,
			}
			for band, count in counts.items()
		]
	)

	if output_table_path:
		output_dir = os.path.dirname(output_table_path)
		if output_dir:
			os.makedirs(output_dir, exist_ok=True)
		table.to_csv(output_table_path, index=False)
		print(f"Saved LLM judge coverage ratio table to: {output_table_path}")
	
	return table


def build_iso_table(filepath: str, output_table_path: str | None = None):
	"""Read ISO 29148 evaluation JSON and return a summary DataFrame highlighting 
	the overall average quality score and issue counts by problem type/dimension.
	"""
	with open(filepath, "r", encoding="utf-8") as jsonfile:
		data = json.load(jsonfile)

	evaluations = data.get("evaluations", []) if isinstance(data, dict) else data
	total_reqs = len(evaluations)

	#return nothing if no things
	if total_reqs == 0:
		table = pd.DataFrame(columns=["category", "problem_type_dimension", "issue_count", "affected_requirements", "average_quality_score", "ratio_or_percentage"])
		return table

	table ={
		"average_quality_score":0,
		"well_formed": 0,
		"problems":0,
		"problem_breakdown":{
			"Singularity" :0,
			"Unambiguity":0,
			"Testability":0,
			"Categorization":0,
			"Completeness":0
		}
	}

	overall_score = 0
	total = 0

	#count of well formed
	for items in evaluations:
		overall_score += items["quality_score"]
		total +=1
		#add to well formed
		if items["is_well_formed"]:
			table['well_formed'] += 1
		else:
			table['problems'] +=1
			for problem in items["issues"]:
				dimension = problem["dimension"]
				table['problem_breakdown'][dimension] +=1

	avg_quality  = overall_score/total
	table['average_quality_score'] = avg_quality
	if output_table_path:
		_write_json_file(output_table_path,table)
	return table


def build_invest_table(filepath: str, output_table_path: str | None = None) -> pd.DataFrame:
	"""Read INVEST user story evaluation JSON and return a summary DataFrame 
	highlighting average scores for each INVEST criterion (I, N, V, E, S, T).
	"""
	with open(filepath, "r", encoding="utf-8") as jsonfile:
		data = json.load(jsonfile)

	evaluations = data.get("evaluations", []) if isinstance(data, dict) else data
	total_stories = len(evaluations)

	if total_stories == 0:
		return pd.DataFrame(columns=["criterion", "average_score"])

	dim_totals = {"independent": 0.0, "negotiable": 0.0, "valuable": 0.0, "estimable": 0.0, "small": 0.0, "testable": 0.0}
	overall_total = 0.0

	for item in evaluations:
		scores = item.get("scores", {}) or {}
		for k in dim_totals:
			dim_totals[k] += float(scores.get(k, 0.0))
		overall_total += float(item.get("overall_invest_score", 0.0))

	rows = [
		{"criterion": "Independent (I)", "average_score": round(dim_totals["independent"] / total_stories, 4)},
		{"criterion": "Negotiable (N)", "average_score": round(dim_totals["negotiable"] / total_stories, 4)},
		{"criterion": "Valuable (V)", "average_score": round(dim_totals["valuable"] / total_stories, 4)},
		{"criterion": "Estimable (E)", "average_score": round(dim_totals["estimable"] / total_stories, 4)},
		{"criterion": "Small (S)", "average_score": round(dim_totals["small"] / total_stories, 4)},
		{"criterion": "Testable (T)", "average_score": round(dim_totals["testable"] / total_stories, 4)},
		{"criterion": "OVERALL INVEST MEAN", "average_score": round(overall_total / total_stories, 4)},
	]

	table = pd.DataFrame(rows)

	if output_table_path:
		output_dir = os.path.dirname(output_table_path)
		if output_dir:
			os.makedirs(output_dir, exist_ok=True)
		table.to_csv(output_table_path, index=False)
		print(f"Saved INVEST evaluation summary table to: {output_table_path}")

	return table

					