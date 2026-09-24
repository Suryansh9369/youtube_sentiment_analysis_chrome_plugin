from huggingface_hub import hf_hub_download
import shutil
from pathlib import Path

repo_id="AmaanP314/youtube-comment-sentiment"
filename = "youtube-comments-sentiment.csv"

dataset_dir= Path("dataset")
dataset_dir.mkdir(parents=True, exist_ok=True)

downloded_file=hf_hub_download(
    repo_id=repo_id,
    filename=filename,
    repo_type="dataset"
)

shutil.copy(downloded_file, dataset_dir/filename)
print(f"Dataset saved to: {dataset_dir/filename}")