from huggingface_hub import HfApi, HfFolder

api = HfApi()
repo_id = 'trampoline/copali_finetuned'
api.create_repo(repo_id, exist_ok=True)
api.upload_folder(folder_path='/models/train_colpali_docmatix_hardneg_ib_3b-mix-448', repo_id=repo_id, repo_type='model')