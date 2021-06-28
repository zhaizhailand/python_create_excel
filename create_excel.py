import xlsxwriter

#创建excel文件
workbook = xlsxwriter.Workbook('data.xlsx')
#创建工作表
worksheet1 = workbook.add_worksheet("操作日志")
#添加工作表样式
bold = workbook.add_format(
{
	'bold': True,#字体加粗
	'border':1,#单元格边框宽度
	'align':'left',#水平对齐方式
	'valign': 'vcenter',#垂直对齐方式
	'fg_color':'#F4B084',#单元格背景颜色
	'text_wrap': True, #是否自动换行
})

#测试数据
expenses = (
	['Rent', 1000],
	['Gas', 100],
	['Food', 300],
	['Gym', 50],
)

# 从首行、首列开始.
row = 0
col = 0
#写入单个单元格数据
#/row:行， col：列， data:要写入的数据, bold:单元格的样式
for item, cost in (expenses):
	worksheet1.write(row, col, item, bold)
	worksheet1.write(row, col + 1, cost, bold)
	row += 1

worksheet1.write(row, 0, 'Total')
worksheet1.write(row, 1, '=SUM(B1:B4)')

#只有此函数才可以生成excel
workbook.close()

