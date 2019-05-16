data=[]
with open('reviews.txt','r') as f:
	#讀取模式r(read) 寫入檔案w(write) 檔案 當作 f(file)

#換行符號\n
	for newfile in f:
		data.append(newfile.strip())
			#.strip()把\n去除掉 只給字串給的功能 .append只給清單用
		#with 夾帶檔案 瞬間開啟open 不會一直開啟檔案 自動close 造成檔案損毀
		#只有在with 裡面 才會oepn 走到第17行時 檔案自動關閉
print(data[0])


