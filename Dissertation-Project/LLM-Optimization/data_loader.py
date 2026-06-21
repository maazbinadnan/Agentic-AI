("""Utilities for loading pickle files and saving as JSON.

Provides `pkl_to_json` which accepts a single .pkl file or a directory
containing .pkl files and writes corresponding .json files.
""")

from pathlib import Path
import pickle
import json
from typing import Any, Optional, List
from dataclasses import is_dataclass, asdict


def _make_serializable(obj: Any) -> Any:
	"""Attempt to convert common non-JSON-serializable objects.

	Fallback to `str(obj)` when no better conversion exists.
	"""
	# Pydantic BaseModel
	try:
		from pydantic import BaseModel

		if isinstance(obj, BaseModel):
			return obj.dict()
	except Exception:
		pass

	# dataclasses
	if is_dataclass(obj):
		return asdict(obj)

	# common containers that may contain non-serializable items
	if isinstance(obj, dict):
		return {str(k): _make_serializable(v) for k, v in obj.items()}
	if isinstance(obj, (list, tuple, set)):
		return [_make_serializable(v) for v in obj]

	# bytes
	if isinstance(obj, (bytes, bytearray)):
		try:
			return obj.decode("utf-8")
		except Exception:
			return list(obj)

	# fallback to string
	try:
		json.dumps(obj)
		return obj
	except Exception:
		return str(obj)


def pkl_to_json(input_path: str | Path, output_dir: Optional[str | Path] = None, *, overwrite: bool = False) -> List[Path]:
	"""Load a .pkl file or all .pkl files in a directory and save them as JSON.

	Args:
		input_path: Path to a .pkl file or directory containing .pkl files.
		output_dir: Directory to write .json files. If None, writes next to each input file.
		overwrite: If False, existing .json files will be skipped.

	Returns:
		List of written JSON file paths.
	"""
	input_path = Path(input_path)
	written: List[Path] = []

	if input_path.is_dir():
		pkl_files = list(input_path.glob("*.pkl"))
	elif input_path.is_file() and input_path.suffix == ".pkl":
		pkl_files = [input_path]
	else:
		raise ValueError(f"Input path must be a .pkl file or directory: {input_path}")

	out_base = Path(output_dir) if output_dir is not None else None
	for pkl in pkl_files:
		try:
			with open(pkl, "rb") as f:
				obj = pickle.load(f)
		except Exception as e:
			# skip files that cannot be unpickled
			continue

		serializable = _make_serializable(obj)

		if out_base is None:
			out_path = pkl.with_suffix(".json")
		else:
			out_base.mkdir(parents=True, exist_ok=True)
			out_path = out_base / (pkl.stem + ".json")

		if out_path.exists() and not overwrite:
			continue

		with open(out_path, "w", encoding="utf-8") as jf:
			json.dump(serializable, jf, ensure_ascii=False, indent=2)

		written.append(out_path)

	return written



def pkl_file_to_json(filepath: str) -> str:
	"""Load a single .pkl file and save it as a .json next to the input.

	Returns the path of the written JSON file.
	"""
	p = Path(filepath)
	if not p.exists() or p.suffix != ".pkl":
		raise ValueError("Provide a valid .pkl filepath")

	with open(p, "rb") as f:
		obj = pickle.load(f)

	serializable = _make_serializable(obj)
	out_path = p.with_suffix(".json")
	with open(out_path, "w", encoding="utf-8") as jf:
		json.dump(serializable, jf, ensure_ascii=False, indent=2)

	return str(out_path)

filepath = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\States\state_before_evaluation.pkl"
pkl_file_to_json(filepath)


filepath = r"C:\Users\OMNI BOOK\OneDrive\Personal-Projects\Agent-Learning\Dissertation-Project\LLM-Optimization\States\\final_state.pkl"
pkl_file_to_json(filepath)
