import bisect  # bisectモジュールをインポート

nums = list(map(int, input().split()))

if not nums:  # 空リストの場合は長さ0
    print(0)
else:
    tails = []  # 「各長さk+1のLISの最小の末尾要素」を格納するリスト
    for num in nums:
        # tailsの中でnum以上の最初の要素の位置を探す (二分探索)
        idx = bisect.bisect_left(tails, num)
        print(idx)
        # もしidxがtailsの長さと同じなら、numはtailsの全要素より大きい
        if idx == len(tails):
            tails.append(num)  # 新しい最長の末尾として追加
        # そうでなければ、tails[idx]をnumで置き換える
        else:
            tails[idx] = num  # より小さい末尾要素に更新

        # デバッグ用: tailsリストの変化を見たければコメントを外す
        print(f"num={num}, tails={tails}")

    # 最終的なtailsリストの長さがLISの長さ
    print(len(tails))
