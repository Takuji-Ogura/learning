# coding:utf-8
# WebCam接続/QRコード読み取りテスト

import cv2
import numpy

def main():
    """メイン処理
    """

    qrd = cv2.QRCodeDetector()
    font = cv2.FONT_HERSHEY_SIMPLEX

    #　カメラ取得
    cam = cv2.VideoCapture(0)
    while True:
        # フレーム取得
        ret, frame = cam.read()

        # QRコード読み取り
        ret, info, points, code = qrd.detectAndDecodeMulti(frame)
        if ret:
            # 座標取得
            points = points.astype(numpy.int)
            for txt, pt in zip(info, points):
                if txt == '': continue

                 # QRコード座標取得
                x = pt[0][0]
                y = pt[0][1]

                # QRコードテキスト描画
                frame = cv2.putText(frame, txt, (x, y-6), font, .3, (0, 0, 255), 1, cv2.LINE_AA)

                # 矩形描画
                frame = cv2.polylines(frame, [pt], True, (0, 255, 0), 1, cv2.LINE_AA)

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
