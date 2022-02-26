from math import ceil,floor
from os import system

print(f"腾讯云轻量优惠券计算器by Nyarime (Build20220227)" + "\n")
print(f"通用型/存储型/企业型任何用户都可以购买，无需企业认证! \n")
print(f"项目地址: https://github.com/Nyarime/qcloud-lighthouse-discount" + "\n")
p = floor(float(input("需续费价格:")))
w = floor(float(input("最低付费门槛:")))
count = 0

saver = input("是否保存结果至LightHouse.txt?(y/n):")
if saver == "y":
    f = open('LightHouse.txt', 'w')
    f.write("腾讯云轻量优惠券计算器 by Nyarime (Build20220227)\n")
    f.write("需续费价格:" + str(p) + "\n")
    f.write("最低付费:" + str(w) + "\n\n")


prices = [
    [32, "非内地通用32元"],
    [42, "非内地通用42元"],
    [54, "非内地通用54元"],
    [67, "非内地通用67元"],
    [100, "非内地通用100元"],
    [133, "非内地通用133元"],
    [54, "非内地通用Windows54元"],
    [72, "非内地通用Windows72元"],
    [96, "非内地通用Windows96元"],
    [121, "非内地通用Windows121元"],
    [180, "非内地通用Windows180元"],
    [239, "非内地通用Windows239元"],
    [258, "非内地企业258元"],
    [405, "非内地企业405元"],
    [590, "非内地企业590元"],
    [780, "非内地企业780元"],
    [1150, "非内地企业1150元"],
    [1520, "非内地企业1520元"],
    [455, "非内地企业Windows455元"],
    [740, "非内地企业Windows740元"],
    [1080, "非内地企业Windows1080元"],
    [1420, "非内地企业Windows1420元"],
    [2100, "非内地企业Windows2100元"],
    [2780, "非内地企业Windows2780元"],
    [50, "内地通用50元"],
    [60, "内地通用60元"],
    [85, "内地通用85元"],
    [100, "内地通用100元"],
    [130, "内地通用130元"],
    [150, "内地通用150元"],
    [105, "内地存储105元"],
    [150, "内地存储150元"],
    [300, "内地存储300元"],
    [255, "内地企业255元"],
    [350, "内地企业350元"],
    [525, "内地企业525元"],
    [700, "内地企业700元"],
    [1050, "内地企业1050元"],
    [1400, "内地企业1400元"],
]

need = w - p
if need < 0:
    if saver == "y":
        f.write("错误，请检查数值是否正确")
    print("错误，请检查数值是否正确")
    system("pause")
    exit()
if need == 0:
    if saver == "y":
        f.write("无需计算，请直接购买产品")
    print("无需计算，请直接购买产品")
    system("pause")
    exit()

print("需计算" + str(need) + "元")

answer = ceil(need / 24) * 24 + p - w

List = list()


def out(data, t):
    dic = dict()
    for item in data:
        if dic.get(item):
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
    if saver == "y":
        f.write("- 需补充" + str(int(t)) + "元,方案: 购买 ")
    print("- 需补充" + str(int(t)) + "元,方案:", end=" 购买 ")
    for item in dic.keys():
        if saver == "y":
            f.write(str(dic[item]) + "月" + item + " ")
        print(str(dic[item]) + "月" + item, end= " ")
    print()
    if saver == "y":
        f.write("\n")


def compute(n):
    global answer, count
    if n <= 0:
        return - n
    for price in prices:
        List.append(price[1])
        t = compute(n - price[0])
        if t is not None:
            if t <= answer:
                out(List, t)
                answer = t
                count += 1
        del List[-1]


compute(need)
print("\n")
print("计算完毕：")
print("已为您生成" + str(count) + "种优化方案")
if saver == "y":
    f.write("\n已生成" + str(count) + "种优化方案\n")
    f.write("项目地址: https://github.com/Nyarime/qcloud-lighthouse-discount")
    f.close()
system("pause")
