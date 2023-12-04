import matplotlib.pyplot as plt

""" #plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0,(1,0)), label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0,(4,1)), label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0,(10,1)), label="PData(km)")

#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="b", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="g", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="lime", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#FF576A", label="Value(m)")

#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=5, solid_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="butt", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, dash_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, dash_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dotted", linewidth=10, solid_capstyle="round", label="Value(m)"
#plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashdot", linewidth=10, dash_capstyle="round", label="Value(m)"
 """




""" # c=cyan d=diamond
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "go-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "co--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "kd-.", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="D", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="x", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$test$", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="$y$", label="PData(km)")


xdata = [2,3,6,7,10]
ydata = [1,4,5,8,9]
y1data = [2,4,6,8,10]

plt.plot(xdata, ydata)

# plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
#plt.fill_between(xdata[:4], ydata[:4], alpha=0.5)
# plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)
#plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

#plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
#plt.fill_betweenx(ydata[:4], xdata[:4], alpha=0.3)

# plt.plot([1,3,5,7,9],[2,4,6,8,10])
plt.plot(xdata, y1data)

#plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
#plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
#plt.fill_between(xdata[:4], ydata[:4], y1data[:4], color = "C2", alpha=0.3)

# plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.1, 5.1], alpha=0.5)
# plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 5.5, 3.1], alpha=0.5)

plt.xlabel("x축")
plt.ylabel("y축")

#plt.legend(ncol=1)
#plt.axis([0,10,0,10])
plt.show() """






""" dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)
#plt.plot([1,4,5,9], [2,3,8,10])

plt.xlabel("x-data")
plt.ylabel("y-data")


# plt.grid()
# plt.grid(axis="x")
# plt.grid(axis="y")
#plt.grid(color="g", alpha=0.5, linestyle="-")
#plt.grid(color="g", alpha=0.5, linestyle="--")

# plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
# plt.grid(axis="x", color="r", alpha=0.3, linestyle="-.")



# plt.xticks()
# plt.yticks()

#plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
#plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.xticks([1,3,5,7,9,11])
# plt.yticks([2,4,6,8,10,12])

# plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# plt.tick_params(axis="x", direction="in")
# plt.tick_params(axis="x", direction="out")
# plt.tick_params(axis="y", direction="in")

plt.show() """




x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["C2", "lime", "#57ADCC"]

# plt.bar(x_years, y_data)


# plt.bar(x_years, y_data, color="g")
# plt.bar(x_years, y_data, color="C7")
# plt.bar(x_years, y_data, color="#57ADCC")

# plt.bar(x_years, y_data, color=clr)

# plt.bar(x_years, y_data, color=clr, width=2)
# plt.bar(x_years, y_data, color=clr, width=0.5)
# plt.bar(x_years, y_data, color=clr, width=0.1)

# plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", width=0.3)

# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="C4", width=0.5)

# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)
# plt.bar(x_years, y_data, color=clr, align="center", edgecolor="blue", linewidth=3, width=0.5)

# plt.yticks([100,200,300,400,500,600,900])





# plt.barh(x_years,y_data)

#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)

plt.show()