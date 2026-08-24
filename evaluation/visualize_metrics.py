import json
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from global_layer.functions import _write_json_file



def coverage_band_from_max_score(max_score: float) -> str:
	"""Map max similarity score to coverage band."""
	if max_score > 0.70:
		return "full_coverage"
	if 0.60 <= max_score <= 0.70:
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


def _load_invest_df(path: str | list[str]) -> pd.DataFrame:
	"""Load INVEST evaluation scores from CSV/JSON file(s). Supports a list of paths to average across multiple runs."""
	if isinstance(path, (list, tuple)):
		dfs = [_load_invest_df(p) for p in path]
		first_df = dfs[0].copy()
		criteria = first_df["criterion"].tolist()
		averaged_rows = []
		for crit in criteria:
			crit_scores = []
			for df in dfs:
				match = df[df["criterion"] == crit]
				if not match.empty:
					crit_scores.append(float(match["average_score"].values[0]))
			avg_score = round(float(np.mean(crit_scores)), 4) if crit_scores else 0.0
			averaged_rows.append({"criterion": crit, "average_score": avg_score})

		res_df = pd.DataFrame(averaged_rows)
		# Ensure overall mean is accurate
		main_scores = res_df[res_df["criterion"] != "OVERALL INVEST MEAN"]["average_score"]
		if (res_df["criterion"] == "OVERALL INVEST MEAN").any() and len(main_scores) > 0:
			res_df.loc[res_df["criterion"] == "OVERALL INVEST MEAN", "average_score"] = round(float(main_scores.mean()), 4)
		return res_df

	if not os.path.exists(path):
		raise FileNotFoundError(f"INVEST evaluation file not found: '{path}'")

	ext = os.path.splitext(path)[1].lower()

	if ext == ".csv":
		df = pd.read_csv(path)
		crit_col = next((c for c in df.columns if "criterion" in str(c).lower()), None)
		if crit_col:
			score_col = next((c for c in df.columns if "score" in str(c).lower()), df.columns[1])
			res_df = pd.DataFrame({
				"criterion": df[crit_col].astype(str),
				"average_score": pd.to_numeric(df[score_col], errors="coerce").fillna(0.0)
			})
			main_scores = res_df[res_df["criterion"] != "OVERALL INVEST MEAN"]["average_score"]
			if (res_df["criterion"] == "OVERALL INVEST MEAN").any():
				ov_val = float(res_df.loc[res_df["criterion"] == "OVERALL INVEST MEAN", "average_score"].values[0]) #type: ignore
				if ov_val == 0.0 and len(main_scores) > 0:
					res_df.loc[res_df["criterion"] == "OVERALL INVEST MEAN", "average_score"] = round(float(main_scores.mean()), 4)
			return res_df

		dim_totals = {"independent": 0.0, "negotiable": 0.0, "valuable": 0.0, "estimable": 0.0, "small": 0.0, "testable": 0.0}
		total_stories = len(df)
		if total_stories > 0:
			for k in dim_totals:
				match_col = next((c for c in df.columns if k in str(c).lower()), None)
				if match_col:
					dim_totals[k] = pd.to_numeric(df[match_col], errors="coerce").mean()

			overall_col = next((c for c in df.columns if "overall" in str(c).lower()), None)
			overall_mean = pd.to_numeric(df[overall_col], errors="coerce").mean() if overall_col else np.mean(list(dim_totals.values()))

			rows = [
				{"criterion": "Independent (I)", "average_score": round(dim_totals["independent"], 4)},
				{"criterion": "Negotiable (N)", "average_score": round(dim_totals["negotiable"], 4)},
				{"criterion": "Valuable (V)", "average_score": round(dim_totals["valuable"], 4)},
				{"criterion": "Estimable (E)", "average_score": round(dim_totals["estimable"], 4)},
				{"criterion": "Small (S)", "average_score": round(dim_totals["small"], 4)},
				{"criterion": "Testable (T)", "average_score": round(dim_totals["testable"], 4)},
				{"criterion": "OVERALL INVEST MEAN", "average_score": round(overall_mean, 4)},
			]
			return pd.DataFrame(rows)

	res_df = build_invest_table(path)
	main_scores = res_df[res_df["criterion"] != "OVERALL INVEST MEAN"]["average_score"]
	if (res_df["criterion"] == "OVERALL INVEST MEAN").any():
		ov_val = float(res_df.loc[res_df["criterion"] == "OVERALL INVEST MEAN", "average_score"].values[0])
		if ov_val == 0.0 and len(main_scores) > 0:
			res_df.loc[res_df["criterion"] == "OVERALL INVEST MEAN", "average_score"] = round(float(main_scores.mean()), 4)
	return res_df


def build_accs_ratio_table(filepath: str, output_table_path: str | None = None) -> pd.DataFrame:
	"""Read ACCS evaluation JSON and return a ratio table for full, partial, and no implementation."""
	with open(filepath, "r", encoding="utf-8") as jsonfile:
		data = json.load(jsonfile)

	total_criteria = data.get("total_criteria_count", 0)
	full_count = data.get("full_count", 0)
	partial_count = data.get("partial_count", 0)
	none_count = data.get("none_count", 0)

	if total_criteria == 0 and "evaluations" in data:
		for story in data.get("evaluations", []):
			for v in story.get("verifications", []):
				total_criteria += 1
				score = float(v.get("verification_score", 0.0))
				if score == 1.0:
					full_count += 1
				elif score == 0.5:
					partial_count += 1
				else:
					none_count += 1

	rows = [
		{
			"implementation_status": "Full Implementation (1.0)",
			"count": full_count,
			"ratio": round(full_count / total_criteria, 4) if total_criteria else 0.0,
		},
		{
			"implementation_status": "Partial Implementation (0.5)",
			"count": partial_count,
			"ratio": round(partial_count / total_criteria, 4) if total_criteria else 0.0,
		},
		{
			"implementation_status": "Non-Implementation (0.0)",
			"count": none_count,
			"ratio": round(none_count / total_criteria, 4) if total_criteria else 0.0,
		},
	]

	table = pd.DataFrame(rows)

	if output_table_path:
		output_dir = os.path.dirname(output_table_path)
		if output_dir:
			os.makedirs(output_dir, exist_ok=True)
		table.to_csv(output_table_path, index=False)
		print(f"Saved ACCS ratio table to: {output_table_path}")

	return table




