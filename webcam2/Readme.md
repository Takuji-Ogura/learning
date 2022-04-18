# cloneしたプロジェクトでvenvを復元して実行する方法

1.  clone
```
$ git clone repo projb
Cloning into 'projb'...
done.
```
2.  venv環境の追加とactivate
```
$ cd projb
$ venv
python -m venv env
$ .\env\Scripts\activate
```
3. パッケージ情報を復元
```
$ pip install -r requirements.txt
Collecting numpy==1.22.3
  Using cached numpy-1.22.3-cp310-cp310-win_amd64.whl (14.7 MB)
Collecting opencv-python==4.5.5.64
  Using cached opencv_python-4.5.5.64-cp36-abi3-win_amd64.whl (35.4 MB)
Installing collected packages: numpy, opencv-python
Successfully installed numpy-1.22.3 opencv-python-4.5.5.64```
```

4. 実行
```
$ python WebcamTest.py
```

