import os
import shutil

os.makedirs("saved_models",exist_ok=True)
shutil.copy(
"checkpoint.pth","saved_models/good_checkpoint_1_.pth"
)
