""" from faker import Faker as fk
import os

#temp = fk()
temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f:
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")
    
with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
            f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")  """







""" import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target) """


""" df["aver"] = df.postcode.rank(method="average")
# print(df[["postcode", "aver"]])

df["dense"] = df.postcode.rank(method="dense")
# print(df[["postcode", "dense"]])

df["first"] = df.postcode.rank(method="first")
# print(df[["postcode", "first"]])

df["min"] = df.postcode.rank(method="min")
# print(df[["postcode", "min"]])

#df["max"] = df.postcode.rank(method="max", ascending= False)
df["max"] = df.postcode.rank(method="max")
#print(df[["postcode", "max"]])
print(df[["postcode", "max", "min", "first", "dense", "aver"]]) """


#전치 컬럼-로우
#print(df.transpose())

#누적계산
#print(df["postcode"].expanding().sum())
#print(df["postcode"].expanding())

# 가장 큰수
#print(df.postcode.idxmax(axis=0)) 
# 가장 작은수
#print(df.postcode.idxmin(axis=0))

#빈 데이터프레임 확인
#print(df.empty)
#print(df.postcode.empty)

#인자 검색
# print(df.isin([41053]))
# print(df.isin(["윤준호"]))
# print(df.isin([41053, 57718]))
# print(df.isin([41053, 57718, "윤준호"]))

#기간 계산
""" period = pd.period_range(start="2023-11-10 00:00:00", end="2023-11-10 02:30:00", freq="30T")
dt = {"col1":[1,2,3,4,5,6],"col2":period}
idx = ["row1","row2","row3","row4","row5","row6"]
pf = pd.DataFrame(data=dt, index=idx)

print(pf) """


#i = pd.date_range("2023-11-10", periods=10, freq="1H")
# i = pd.date_range("2023-11-10", periods=10, freq="3H")
# df = pd.DataFrame({"col1":[1,2,3,4,5,6,7,8,9,10]}, index=i)
# print(df)

# print("\n-----------------------------\n")
#print(df.at_time("09:00"))
#print(df.at_time("03:00"))

#print(df.between_time(start_time="12:00", end_time="00:00"))
# print(df.between_time(start_time="03:00", end_time="09:00"))




""" #i = pd.date_range("2023-11-10", periods=10, freq="3D")
i = pd.date_range("2023-11-10", periods=10, freq="5D")
df = pd.DataFrame({'col1':[1,2,3,4,5,6,7,8,9,10]}, index=i)
print(df)

print("\n-----------------------------\n")
#print(df.first("5D"))
#print(df.first("7D"))
#print(df.last("3D"))
print(df.last("7D")) """




#=========================================================

""" import FinanceDataReader as fdr

# ksp = fdr.DataReader("KS11", "2023")
ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n-----------------------------\n")



# res = ksp["High"].max()
# print(res)
# res = ksp["High"].idxmax()
# print(res)


# res = ksp["Low"].min()
# print(res)
# res = ksp["Low"].idxmin()
# print(res)


# res = ksp["Volume"].nlargest(n=5)
# res = ksp["Volume"].nlargest(n=10)
# print(res)

#res = ksp["Volume"].nsmallest(n=5)
#res = ksp["Close"].nsmallest(n=5)
# res = ksp["Close"].nlargest(n=5)
# print(res)



# cond = ksp["Close"] >= 3000
# cond = ksp["Close"] >= 2000
# res = ksp[cond].index[0]
# print(res)


# res = ksp["Volume"] > ksp["Volume"].shift()
# print(res)

ksp["up"] = ksp["Volume"] > ksp["Volume"].shift()
# print(ksp)

# res = ksp["up"] != ksp["up"].shift().cumsum()
# print(res)

ksp["grp"] = (ksp["up"] != ksp["up"].shift()).cumsum()
# print(ksp)

ksp["up_cnt"] = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
#print(ksp)

print(ksp["up_cnt"].max()) """




#===================================================

""" import pandas as pd

target = "./data/apt.csv"
df = pd.read_csv(target, encoding="CP949")
df.to_csv("./data/conv_apt.csv", encoding="utf8")

print(df.head()) """




import pandas as pd

df = pd.read_csv("./data/conv_apt.csv", index_col= 0)
print(df.head())
print("\n-----------------------------\n")

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
#print(df)
#print(df.dtypes)

df["분양가"] = df["분양가"].convert_dtypes()
#print(df.dtypes)

#arr = df.to_numpy()
#print(arr)
#print(arr[2])
#print(len(arr))

#print(df.describe())

print(df.transpose())
print("\n-----------------------------\n")
print(df.T.head())