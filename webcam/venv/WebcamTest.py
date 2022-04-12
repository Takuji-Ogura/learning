# coding:utf-8
# WebCam接続テスト

import cv2

def main():
    """メイン処理
    """

    #　カメラ取得
    cam = cv2.VideoCapture(0)
    while True:
        # フレーム取得
        ret, frame = cam.read()

        # イメージ描画
        cv2.imshow('Web Camera', frame)
 
        # Qキーでループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'): break
 
    #　カメラ解放
    cam.release()

    # ウィンドウを閉じる
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
