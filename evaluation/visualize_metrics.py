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


def _load_invest_df(path: str) -> pd.DataFrame:
	"""Load INVEST evaluation scores from either a summary CSV, raw story CSV, or JSON evaluation file."""
	if not os.path.exists(path):
		raise FileNotFoundError(f"INVEST evaluation file not found: '{path}'")

	ext = os.path.splitext(path)[1].lower()

	if ext == ".csv":
		df = pd.read_csv(path)
		cols_lower = [str(c).lower().strip() for c in df.columns]
		if "criterion" in cols_lower:
			crit_col = df.columns[cols_lower.index("criterion")]
			score_col = df.columns[cols_lower.index("average_score")] if "average_score" in cols_lower else df.columns[1]
			return pd.DataFrame({
				"criterion": df[crit_col].astype(str),
				"average_score": pd.to_numeric(df[score_col], errors="coerce").fillna(0.0)
			})

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

	return build_invest_table(path)


def plot_invest_comparison(
	file_paths: list[str] | dict[str, str],
	labels: list[str] | None = None,
	output_image_path: str = "invest_comparison_barchart.png",
	title: str = "INVEST Criteria Evaluation Comparison Across Designs",
	include_overall: bool = True,
) -> str:
	"""Generate a grouped bar chart comparing mean INVEST criteria scores across three designs.

	Parameters
	----------
	file_paths : list[str] | dict[str, str]
		A list of 3 (or more) CSV or JSON file paths or a dict mapping {design_label: file_path}.
	labels : list[str] | None
		Custom labels for each design if file_paths is provided as a list.
	output_image_path : str
		Target output path for the saved bar chart image (.png / .pdf).
	title : str
		Chart title.
	include_overall : bool
		Whether to include the 'OVERALL INVEST MEAN' bar group alongside individual criteria.

	Returns
	-------
	str
		Path to the saved bar chart image.
	"""
	if isinstance(file_paths, dict):
		design_files = file_paths
	elif isinstance(file_paths, (list, tuple)):
		if labels and len(labels) == len(file_paths):
			design_files = dict(zip(labels, file_paths))
		else:
			design_files = {f"Design {i+1}": path for i, path in enumerate(file_paths)}
	else:
		raise ValueError("file_paths must be a list of file paths or a dict of {label: file_path}.")

	design_dfs = {}
	for label, path in design_files.items():
		df = _load_invest_df(path)
		if not include_overall:
			df = df[df["criterion"] != "OVERALL INVEST MEAN"].reset_index(drop=True)
		design_dfs[label] = df


	first_label = next(iter(design_dfs))
	criteria = design_dfs[first_label]["criterion"].tolist()

	num_criteria = len(criteria)
	num_designs = len(design_dfs)
	x = np.arange(num_criteria)
	bar_width = 0.8 / max(num_designs, 1)

	fig, ax = plt.subplots(figsize=(13, 6))
	colors = ["#2b5c8f", "#e05d06", "#2a9d8f", "#9b59b6", "#e74c3c"]

	for i, (design_label, df) in enumerate(design_dfs.items()):
		score_map = dict(zip(df["criterion"], df["average_score"]))
		scores = [score_map.get(c, 0.0) for c in criteria]
		offset = x + (i - (num_designs - 1) / 2) * bar_width
		bars = ax.bar(
			offset,
			scores,
			bar_width,
			label=design_label,
			color=colors[i % len(colors)],
			edgecolor="black",
			linewidth=0.8,
		)

		for bar in bars:
			height = bar.get_height()
			ax.annotate(
				f"{height:.2f}",
				xy=(bar.get_x() + bar.get_width() / 2, height),
				xytext=(0, 3),
				textcoords="offset points",
				ha="center",
				va="bottom",
				fontsize=8,
				fontweight="bold",
			)

	ax.set_ylabel("Mean Criterion Score", fontsize=12, fontweight="bold")
	ax.set_title(title, fontsize=14, fontweight="bold", pad=15)
	ax.set_xticks(x)
	ax.set_xticklabels(criteria, rotation=15, ha="right", fontsize=10, fontweight="bold")
	ax.legend(title="Designs", title_fontsize="11", loc="upper left", frameon=True)
	ax.set_ylim(0, 1.18)
	ax.grid(axis="y", linestyle="--", alpha=0.5)

	plt.tight_layout()

	output_dir = os.path.dirname(output_image_path)
	if output_dir:
		os.makedirs(output_dir, exist_ok=True)

	plt.savefig(output_image_path, dpi=300, bbox_inches="tight")
	plt.close()

	print(f"Saved INVEST comparison bar chart to: {output_image_path}")
	return output_image_path


def _load_coverage_df(path: str) -> pd.DataFrame:
	"""Load Embedding Coverage ratio DataFrame from CSV or JSON file."""
	if not os.path.exists(path):
		raise FileNotFoundError(f"Coverage file not found: '{path}'")

	ext = os.path.splitext(path)[1].lower()
	if ext == ".csv":
		df = pd.read_csv(path)
		band_col = next((c for c in df.columns if "band" in str(c).lower() or "verdict" in str(c).lower() or "coverage" in str(c).lower()), df.columns[0])
		ratio_col = next((c for c in df.columns if "ratio" in str(c).lower()), df.columns[-1])
		return pd.DataFrame({
			"coverage_band": df[band_col].astype(str),
			"ratio": pd.to_numeric(df[ratio_col], errors="coerce").fillna(0.0)
		})

	return build_coverage_ratio_table(path)


def plot_coverage_comparison(
	file_paths: list[str] | dict[str, str],
	labels: list[str] | None = None,
	output_image_path: str = "coverage_comparison_barchart.png",
	title: str = "Embedding Coverage Ratio Comparison Across Designs",
) -> str:
	"""Generate a grouped bar chart comparing Embedding Coverage ratios (Full, Partial, No Coverage) across three designs.

	Parameters
	----------
	file_paths : list[str] | dict[str, str]
		A list of 3 (or more) CSV or JSON file paths or a dict mapping {design_label: file_path}.
	labels : list[str] | None
		Custom labels for each design if file_paths is provided as a list.
	output_image_path : str
		Target output path for the saved bar chart image (.png / .pdf).
	title : str
		Chart title.

	Returns
	-------
	str
		Path to the saved bar chart image.
	"""
	if isinstance(file_paths, dict):
		design_files = file_paths
	elif isinstance(file_paths, (list, tuple)):
		if labels and len(labels) == len(file_paths):
			design_files = dict(zip(labels, file_paths))
		else:
			design_files = {f"Design {i+1}": path for i, path in enumerate(file_paths)}
	else:
		raise ValueError("file_paths must be a list of file paths or a dict of {label: file_path}.")

	design_dfs = {label: _load_coverage_df(path) for label, path in design_files.items()}

	std_bands = ["full_coverage", "partial_coverage", "no_coverage"]
	display_labels = ["Full Coverage", "Partial Coverage", "No Coverage"]

	num_bands = len(std_bands)
	num_designs = len(design_dfs)
	x = np.arange(num_bands)
	bar_width = 0.8 / max(num_designs, 1)

	fig, ax = plt.subplots(figsize=(11, 6))
	colors = ["#2b5c8f", "#e05d06", "#2a9d8f", "#9b59b6", "#e74c3c"]

	for i, (design_label, df) in enumerate(design_dfs.items()):
		ratio_map = {}
		for _, row in df.iterrows():
			band_name = str(row.iloc[0]).lower().strip()
			ratio_val = float(row.get("ratio", row.iloc[-1]))
			ratio_map[band_name] = ratio_val

		ratios = [ratio_map.get(b, ratio_map.get(b.replace("_coverage", ""), 0.0)) for b in std_bands]
		offset = x + (i - (num_designs - 1) / 2) * bar_width
		bars = ax.bar(
			offset,
			ratios,
			bar_width,
			label=design_label,
			color=colors[i % len(colors)],
			edgecolor="black",
			linewidth=0.8,
		)

		for bar in bars:
			height = bar.get_height()
			ax.annotate(
				f"{height:.4f}",
				xy=(bar.get_x() + bar.get_width() / 2, height),
				xytext=(0, 3),
				textcoords="offset points",
				ha="center",
				va="bottom",
				fontsize=8,
				fontweight="bold",
			)

	ax.set_ylabel("Coverage Ratio", fontsize=12, fontweight="bold")
	ax.set_title(title, fontsize=14, fontweight="bold", pad=15)
	ax.set_xticks(x)
	ax.set_xticklabels(display_labels, fontsize=11, fontweight="bold")
	ax.legend(title="Designs", title_fontsize="11", loc="upper right", frameon=True)
	ax.set_ylim(0, 1.15)
	ax.grid(axis="y", linestyle="--", alpha=0.5)

	plt.tight_layout()

	output_dir = os.path.dirname(output_image_path)
	if output_dir:
		os.makedirs(output_dir, exist_ok=True)

	plt.savefig(output_image_path, dpi=300, bbox_inches="tight")
	plt.close()

	print(f"Saved embedding coverage comparison bar chart to: {output_image_path}")
	return output_image_path


def _load_coverage_llm_df(path: str) -> pd.DataFrame:
	"""Load LLM Judge Coverage ratio DataFrame from CSV or JSON file."""
	if not os.path.exists(path):
		raise FileNotFoundError(f"LLM Coverage file not found: '{path}'")

	ext = os.path.splitext(path)[1].lower()
	if ext == ".csv":
		df = pd.read_csv(path)
		band_col = next((c for c in df.columns if "verdict" in str(c).lower() or "band" in str(c).lower() or "coverage" in str(c).lower()), df.columns[0])
		ratio_col = next((c for c in df.columns if "ratio" in str(c).lower()), df.columns[-1])
		return pd.DataFrame({
			"coverage_verdict": df[band_col].astype(str),
			"ratio": pd.to_numeric(df[ratio_col], errors="coerce").fillna(0.0)
		})

	return build_coverage_llm_ratio_table(path)


def plot_coverage_llm_comparison(
	file_paths: list[str] | dict[str, str],
	labels: list[str] | None = None,
	output_image_path: str = "coverage_llm_comparison_barchart.png",
	title: str = "LLM Judge Coverage Ratio Comparison Across Designs",
) -> str:
	"""Generate a grouped bar chart comparing LLM Judge Coverage ratios (Full, Partial, No Coverage) across three designs.

	Parameters
	----------
	file_paths : list[str] | dict[str, str]
		A list of 3 (or more) CSV or JSON file paths or a dict mapping {design_label: file_path}.
	labels : list[str] | None
		Custom labels for each design if file_paths is provided as a list.
	output_image_path : str
		Target output path for the saved bar chart image (.png / .pdf).
	title : str
		Chart title.

	Returns
	-------
	str
		Path to the saved bar chart image.
	"""
	if isinstance(file_paths, dict):
		design_files = file_paths
	elif isinstance(file_paths, (list, tuple)):
		if labels and len(labels) == len(file_paths):
			design_files = dict(zip(labels, file_paths))
		else:
			design_files = {f"Design {i+1}": path for i, path in enumerate(file_paths)}
	else:
		raise ValueError("file_paths must be a list of file paths or a dict of {label: file_path}.")

	design_dfs = {label: _load_coverage_llm_df(path) for label, path in design_files.items()}

	std_bands = ["full_coverage", "partial_coverage", "no_coverage"]
	display_labels = ["Full Coverage", "Partial Coverage", "No Coverage"]

	num_bands = len(std_bands)
	num_designs = len(design_dfs)
	x = np.arange(num_bands)
	bar_width = 0.8 / max(num_designs, 1)

	fig, ax = plt.subplots(figsize=(11, 6))
	colors = ["#2b5c8f", "#e05d06", "#2a9d8f", "#9b59b6", "#e74c3c"]

	for i, (design_label, df) in enumerate(design_dfs.items()):
		ratio_map = {}
		for _, row in df.iterrows():
			band_name = str(row.iloc[0]).lower().strip()
			ratio_val = float(row.get("ratio", row.iloc[-1]))
			ratio_map[band_name] = ratio_val

		ratios = [ratio_map.get(b, ratio_map.get(b.replace("_coverage", ""), 0.0)) for b in std_bands]
		offset = x + (i - (num_designs - 1) / 2) * bar_width
		bars = ax.bar(
			offset,
			ratios,
			bar_width,
			label=design_label,
			color=colors[i % len(colors)],
			edgecolor="black",
			linewidth=0.8,
		)

		for bar in bars:
			height = bar.get_height()
			ax.annotate(
				f"{height:.4f}",
				xy=(bar.get_x() + bar.get_width() / 2, height),
				xytext=(0, 3),
				textcoords="offset points",
				ha="center",
				va="bottom",
				fontsize=8,
				fontweight="bold",
			)

	ax.set_ylabel("Coverage Ratio", fontsize=12, fontweight="bold")
	ax.set_title(title, fontsize=14, fontweight="bold", pad=15)
	ax.set_xticks(x)
	ax.set_xticklabels(display_labels, fontsize=11, fontweight="bold")
	ax.legend(title="Designs", title_fontsize="11", loc="upper right", frameon=True)
	ax.set_ylim(0, 1.15)
	ax.grid(axis="y", linestyle="--", alpha=0.5)

	plt.tight_layout()

	output_dir = os.path.dirname(output_image_path)
	if output_dir:
		os.makedirs(output_dir, exist_ok=True)

	plt.savefig(output_image_path, dpi=300, bbox_inches="tight")
	plt.close()

	print(f"Saved LLM judge coverage comparison bar chart to: {output_image_path}")
	return output_image_path


if __name__ == "__main__":
	evals_base = os.path.join(os.path.dirname(__file__), "evals")

	# 1. INVEST Comparison Bar Chart Call
	plot_invest_comparison(
		file_paths=[
			os.path.join(evals_base, "single_final", "single_final_invest_table.csv"),
			os.path.join(evals_base, "rc_final", "rc_final_invest_table.csv"),
			os.path.join(evals_base, "hitl_final", "hitl_final_invest_table.csv"),
		],
		labels=["Single Agent", "Supervisor-Worker", "HITL Agent"],
		output_image_path=os.path.join(evals_base, "invest_comparison_barchart.png"),
		title="INVEST Criteria Evaluation Comparison Across Designs",
	)

	# 2. Embedding Coverage Ratio Comparison Bar Chart Call
	plot_coverage_comparison(
		file_paths=[
			os.path.join(evals_base, "single_final", "single_final_coverage_ratio_table.csv"),
			os.path.join(evals_base, "rc_final", "rc_final_coverage_ratio_table.csv"),
			os.path.join(evals_base, "hitl_final", "hitl_final_coverage_ratio_table.csv"),
		],
		labels=["Single Agent", "Supervisor-Worker", "HITL Agent"],
		output_image_path=os.path.join(evals_base, "coverage_comparison_barchart.png"),
		title="Embedding Coverage Ratio Comparison Across Designs",
	)

	# 3. LLM Judge Coverage Ratio Comparison Bar Chart Call
	plot_coverage_llm_comparison(
		file_paths=[
			os.path.join(evals_base, "single_final", "single_final_llm_eval_table.csv"),
			os.path.join(evals_base, "rc_final", "rc_final_llm_eval_table.csv"),
			os.path.join(evals_base, "hitl_final", "hitl_final_llm_eval_table.csv"),
		],
		labels=["Single Agent", "Supervisor-Worker", "HITL Agent"],
		output_image_path=os.path.join(evals_base, "coverage_llm_comparison_barchart.png"),
		title="LLM Judge Coverage Ratio Comparison Across Designs",
	)