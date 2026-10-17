from pathlib import Path
import subprocess
root=Path(__file__).resolve().parents[1]
tracked=subprocess.check_output(['git','ls-files'],cwd=root,text=True).splitlines()
assert not any(Path(p).suffix.lower() in {'.jpg','.jpeg','.png','.webp','.npy','.npz','.onnx'} for p in tracked)
candidates=['data/person_01/photo.jpg','embeddings/person_01.npy','metadata/people.json','logs.json']
for p in candidates:
    result=subprocess.run(['git','check-ignore','--no-index',p],cwd=root,capture_output=True,text=True)
    assert result.returncode==0,p
    print('Ignored:',p)
print('PASS: no tracked photographs/biometric arrays/model weights; representative private records ignored.')
print('Documentation-only repository: no executable system or recognition accuracy result.')
