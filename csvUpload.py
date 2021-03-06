import csv
import MySQLdb

mydb=MySQLdb.connect(host="localhost",user="root",password="root",database="mobile1")

displayQuery="select * from mobile_display where Screen_size =  '";
mobileDisplay_insert="insert ignore into mobile_display(Screen_size,Resolution) values (%s,%s)"
selectMobile="select * from mobile_mobile1 where Brand = '";
mobile_insert = "insert ignore into mobile_mobile1(Brand,ProductName,display_id,camera_id,ram_id,processor_id,battery_id,big_img0,big_img1,big_img2,big_img3,big_img4,big_img5,big_img6,img,storage_info,display_info,cam_info,battery_info,processor_info,display_type,link,Product_price,Product_rating,about_phone) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ";
batteryQuery="select * from mobile_battery where capacity = '";
mobileBattery_insert="insert ignore into mobile_battery(Capacity) values (%s)";
processorQuery="select * from mobile_processor where OS = '";
mobileProcessor_insert="insert ignore into mobile_processor(OS,freq) values (%s,%s)";
cameraQuery="select * from mobile_camera where Primary_cam = '";
mobileCamera_insert="insert ignore into mobile_camera(Primary_cam,Secondary_cam) values (%s,%s)";
ramQuery="select * from mobile_RAM where ram = '";
mobileRAM_insert="insert ignore into mobile_RAM(ram) values (%s)";
displayid_select="select id from mobile_display where Screen_size = '";
batteryid_select="select id from mobile_battery where capacity = '";
processorid_select="select id from mobile_processor where OS = '";
cameraid_select="select id from mobile_camera where Primary_cam = '";
ramid_select="select id from mobile_ram where ram = '";

def InsertCSV():
	with open("C:/Users/Aryan/Project/mobile.csv",encoding="utf8")as csv_file:
		csvfile = csv.reader(csv_file,delimiter=',')
		next(csvfile)
		all_value=[]
		all_mob_value=[]
		bat_val=[]
		all_bat_val=[]
		pro_val=[]
		all_pro_val=[]
		cam_val=[]
		all_cam_val=[]
		ram_val=[]
		all_ram_val=[]

		for row in csvfile:
			mycursor=mydb.cursor()
			battery=row[0].strip();
			brand=row[2].strip();
			display_resolution=row[4].strip();
			display_size=row[5].strip();
			os=row[7].strip();
			primary_cam=row[9].strip();
			processor=row[10].strip();
			big_img0=row[11].strip();
			big_img1=row[12].strip();
			big_img2=row[13].strip();
			big_img3=row[14].strip();
			big_img4=row[15].strip();
			big_img5=row[16].strip();
			big_img6=row[17].strip();
			img=row[18].strip();
			name=row[19].strip();
			price=row[20].strip();
			rating=row[21].strip();
			ram=row[22].strip();
			secondary_cam=row[23].strip();
			aboutphone=row[26].strip();
			storage_info=row[27].strip();
			display_info=row[28].strip();
			cam_info=row[29].strip();
			battery_info=row[30].strip();
			processor_info=row[31].strip();
			display_type=row[32].strip();
			link=row[34].strip();
			
			#Display table
			value=(display_size,display_resolution)
			mycursor.execute(displayQuery + display_size + "' and Resolution = '" + display_resolution + "'")
			row_count=mycursor.rowcount
			#print(row_count)
			if row_count==0:
				all_value.append(value)
				mycursor.execute(mobileDisplay_insert,value)
				mydb.commit()
				
			#Battery table
			bat_val=(battery)
			mycursor.execute(batteryQuery + battery +"'")
			row_count2=mycursor.rowcount
			if row_count2==0:
				all_bat_val.append(bat_val)
				#print(bat_val)
				mycursor.execute(mobileBattery_insert,(bat_val,))
				mydb.commit()
				
			#Processor table
			pro_val=(os,processor)
			mycursor.execute(processorQuery + os + "' and freq = '" + processor + "'")
			row_count3=mycursor.rowcount
			if row_count3==0:
				all_pro_val.append(pro_val)
				mycursor.execute(mobileProcessor_insert,pro_val)
				mydb.commit()
				
			#Camera Table
			cam_val=(primary_cam,secondary_cam)
			mycursor.execute(cameraQuery + primary_cam + "' and Secondary_cam = '" + secondary_cam + "'")
			row_count4=mycursor.rowcount
			if row_count4==0:
				all_cam_val.append(cam_val)
				mycursor.execute(mobileCamera_insert,cam_val)
				mydb.commit()
				
			#RAM table
			ram_val=(ram)
			mycursor.execute(ramQuery + ram +"'")
			row_count5=mycursor.rowcount
			if row_count5==0:
				all_ram_val.append(ram_val)
				mycursor.execute(mobileRAM_insert,(ram_val,))
				mydb.commit()
			
			#Mobile table	
			mycursor.execute(displayid_select + display_size + "' and Resolution = '" + display_resolution + "'")
			output=mycursor.fetchall()
			displayid=output[0][0]
			mycursor.execute(batteryid_select + battery + "'")
			output1=mycursor.fetchall()
			batteryid=output1[0][0]
			mycursor.execute(processorid_select + os + "' and freq = '" + processor + "'")
			output2=mycursor.fetchall()
			processorid=output2[0][0]
			mycursor.execute(cameraid_select + primary_cam + "' and Secondary_cam = '" + secondary_cam + "'")
			output3=mycursor.fetchall()
			cameraid=output3[0][0]
			mycursor.execute(ramid_select + ram + "'")
			output4=mycursor.fetchall()
			ramid=output4[0][0]
			#print(displayid)
			#Brand,ProductName,display_id,camera_id,ram_id,processor_id,battery_id,big_img0,big_img1,big_img2,big_img3,big_img4,big_img5,big_img6,img,storage_info,display_info,cam_info,battery_info,processor_info,display_type,link,Product_price,Product_rating,about_phone
			mob_value=(brand,name,displayid,cameraid,ramid,processorid,batteryid,big_img0,big_img1,big_img2,big_img3,big_img4,big_img5,big_img6,img,storage_info,display_info,cam_info,battery_info,processor_info,display_type,link,price,rating,aboutphone)
			#print(selectMobile + brand + "' and ProductName = '" + name + "' and display_id = '" + str(displayid) + "' and battery_id = '" + str(batteryid) + "' and processor_id = '" + str(processorid) + "' and camera_id = '" + str(cameraid) + "' and ram_id = '" + str(ramid) + "' and big_img0 = '" + big_img0 + "' and big_img1 = '" + big_img1 + "' and big_img2 = '" + big_img2 + "' and big_img3 = '" + big_img3 + "' and big_img4 = '" + big_img4 + "' and big_img5 = '" + big_img5 + "' and big_img6 = '" + big_img6 + "' and img = '" + img + "' and Product_price = '" + price + "' and Product_rating = '" + rating + "' and about_phone = '" + aboutphone + "' and storage_info = '" + storage_info + "' and disc2 = '" + display_info + "' and disc3 = '" + cam_info + "' and disc4 = '" + battery_info + "' and disc5 = '" + processor_info + "' and disc6 = '" + display_type + "' and disc7 = '" + row[33] + "' and link = '" + link + "'")
			aboutphone=aboutphone.replace("'","''")
			mycursor.execute(selectMobile + brand + "' and ProductName = '" + name + "' and display_id = '" + str(displayid) + "' and camera_id = '" + str(cameraid) + "' and ram_id = '" + str(ramid) + "' and processor_id = '" + str(processorid) + "' and battery_id = '" + str(batteryid) + "' and big_img0 = '" + big_img0 + "' and big_img1 = '" + big_img1 + "' and big_img2 = '" + big_img2 + "' and big_img3 = '" + big_img3 + "' and big_img4 = '" + big_img4 + "' and big_img5 = '" + big_img5 + "' and big_img6 = '" + big_img6 + "' and img = '" + img + "' and storage_info = '" + storage_info + "' and display_info = '" + display_info + "' and cam_info = '" + cam_info + "' and battery_info = '" + battery_info + "' and processor_info = '" + processor_info + "' and display_type = '" + display_type + "' and link = '" + link + "' and Product_price = '" + price + "' and Product_rating = '" + rating + "' and about_phone = '" + aboutphone + "'")
			row_count1=mycursor.rowcount
			print(row_count1)
			if row_count1==0:
				all_mob_value.append(mob_value)
				mycursor.execute(mobile_insert,mob_value)
				mydb.commit()
				
InsertCSV()