import h5py

#difference=[['new=qcd1000to1500_1.h5 old=data_1.h5'],['new_start','new_end','old-new'],[0,42,'none'], [43,98,985],[99,1126,-99],[1127,1226,775], [1227,2044,-143], [2045,2137,886], [2138,3066,-136], [3067,3167,571], [3168,3781,-144],[3782,3855,'none'],[3856,4095,-117]]
difference=[['new=qcd1000to1500_1.h5 old=data_1.h5'], ['new_start', 'new_end', 'old-new'], [0, 42, 'none'], [43, 98, 985], [99, 1126, -99], [1127, 1226, 775], [1227, 2044, -143], [2045, 2137, 886], [2138, 3066, -136], [3067, 3167, 571], [3168, 3781, -144], [3782, 3855, 'none'], [3856, 4095, -117], ['new=qcd1000to1500_2.h5 old=data_2.h5'], ['new_start', 'new_end', 'old-new'], [0, 116, 'none'], [117, 369, -117], [370, 478, 833], [479, 1354, -152], [1355, 1459, 618], [1460, 2120, -148], [2121, 2198, 1008], [2199, 3249, -121], [3250, 3350, 'none'], [3351, 4095, -144], ['new=qcd1000to1500_3.h5 old=data_3.h5'], ['new_start', 'new_end', 'old-new'], [0, 143, 'none'], [144, 172, -144], [173, 202, 932], [203, 1177, -73], [1178, 1280, 1007], [1281, 1396, 0], [1397, 1499, -219], [1500, 2287, -103], [2288, 2302, 854], [2303, 3156, -15], [3157, 3243, 'none'], [3244, 4095, -87], ['new=qcd1000to1500_4.h5 old=data_4.h5'], ['new_start', 'new_end', 'old-new'], [0, 86, 'none'], [87, 98, -87], [99, 187, 809], [188, 996, -89], [997, 1098, 884], [1099, 1982, -102], [1983, 2045, 912], [2046, 2957, -63], [2958, 3064, 729], [3065, 3793, -107], [3794, 3855, 'none'], [3856, 4095, -62], ['new=qcd1000to1500_5.h5 old=data_5.h5'], ['new_start', 'new_end', 'old-new'], [0, 61, 'none'], [62, 667, -62], [668, 4095, 0]]

for i in range(2,6):
  new=h5py.File('/home/swkim/test_preprocess_new/trackpt_hdf5_32PU_224x224/QCDBkg/HT1000to1500/qcd1000to1500_'+str(i)+'.h5','r')
  old=h5py.File('/data/swkim/trackPt_nchw/hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(i)+'.h5','r')
  difference.append(['new=qcd1000to1500_'+str(i)+'.h5 old='+'data_'+str(i)+'.h5'])
  difference.append(['new_start','new_end','old-new'])
  new_images=new['all_events']['images']
  old_images=old['all_events']['images']
  
  #data_1.h5
  
  
  temp_diff=[0,0,0]
  
  #for i in range(2514,4096):
  i=0
  while(i<4096):
    
    for j in range(4096):
    
  
      if (new_images[i,0,:,:]==old_images[j,0,:,:]).all():
        if temp_diff[2]=='none':
          difference.append(temp_diff.copy())
          print(difference)
        temp_diff[0]=i
        #temp_diff[1]=i
        temp_diff[2]=j-i
        diff=temp_diff[2]
        print('new=',i,'old=',j)
        while( i+1<4096 and (new_images[i+1,0,:,:]==old_images[i+1+diff,0,:,:]).all()):
          i=i+1
          print('new=',i,'old=',i+diff)
        temp_diff[1]=i
        difference.append(temp_diff.copy())
        print(difference)
        break
        
      elif j==4095:
        if temp_diff[2]=='none':
          temp_diff[1]=i
        else:
          temp_diff[0]=i
          temp_diff[1]=i
          temp_diff[2]='none'
        print('new=',i,'old=none')
    i=i+1

#########################################################3
'''
new=h5py.File('/home/swkim/test_preprocess_new/trackpt_hdf5_32PU_224x224/QCDBkg/HT1000to1500/qcd1000to1500_'+str(1)+'.h5','r')
old=h5py.File('/data/swkim/trackPt_nchw/hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(3)+'.h5','r')
difference.append(['new=qcd1000to1500_'+str(i)+'.h5 old='+'data_'+str(i)+'.h5'])
difference.append(['new_start','new_end','old-new'])
new_images=new['all_events']['images']
old_images=old['all_events']['images']
for j in range(4096):
  if (new_images[3250,0]==old_images[j,0]).all():
    print(j)
    break
#################################################################
difference=[['new=qcd1000to1500_1.h5 old=data_1.h5'], ['new_start', 'new_end', 'old-new'], [0, 42, 'none'], [43, 98, 985], [99, 1126, -99], [1127, 1226, 775], [1227, 2044, -143], [2045, 2137, 886], [2138, 3066, -136], [3067, 3167, 571], [3168, 3781, -144], [3782, 3855, 'none'], [3856, 4095, -117], ['new=qcd1000to1500_2.h5 old=data_2.h5'], ['new_start', 'new_end', 'old-new'], [0, 116, 'none'], [117, 369, -117], [370, 478, 833], [479, 1354, -152], [1355, 1459, 618], [1460, 2120, -148], [2121, 2198, 1008], [2199, 3249, -121], [3250, 3350, 'none'], [3351, 4095, -144], ['new=qcd1000to1500_3.h5 old=data_3.h5'], ['new_start', 'new_end', 'old-new'], [0, 143, 'none'], [144, 172, -144], [173, 202, 932], [203, 1177, -73], [1178, 1280, 1007], [1281, 1396, 0], [1397, 1499, -219], [1500, 2287, -103], [2288, 2302, 854], [2303, 3156, -15], [3157, 3243, 'none'], [3244, 4095, -87], ['new=qcd1000to1500_4.h5 old=data_4.h5'], ['new_start', 'new_end', 'old-new'], [0, 86, 'none'], [87, 98, -87], [99, 187, 809], [188, 996, -89], [997, 1098, 884], [1099, 1982, -102], [1983, 2045, 912], [2046, 2957, -63], [2958, 3064, 729], [3065, 3793, -107], [3794, 3855, 'none'], [3856, 4095, -62], ['new=qcd1000to1500_5.h5 old=data_5.h5'], ['new_start', 'new_end', 'old-new'], [0, 61, 'none'], [62, 667, -62], [668, 4095, 0]]

data=[]
for i in difference:
  if len(i)==1:
    data.append(i[:])
  elif i[0]=='new_start':
    i.append('old_start')
    i.append('old_end')
    data.append(i[:])
  else:
    if type(i[2])!='str'
      i.append(i[0]+i[2])
      i.append(i[1]+i[2])
      data.append(i[:])


for i in data:
  try:
    print('{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}'.format(i[0],i[1],i[2],i[3],i[4]))
  except:
    print('{0:>10}'.format(i[0]))

'''
#for i in range(1,13):
	#d=h5py.File('/xrootd/store/user/jiwoong/HEP_CNN_Large_Image/hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(i)+'.h5', 'r')
	#d=h5py.File('/xrootd/store/user/hnam/sample4Nurion/2018DAS/Delphes/presel/hdf5_32PU_224x224/RPV/Gluino1400GeV/0000/RPV_1400-'+str(i)+'.h5', 'r')
  # ui20

  #d=h5py.File('/store/local1/users/jhgoh/nurion4hep/20200808_2/hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(i)+'.h5', 'r')
	# khu
  
  #print('data_'+str(i)+'.h5')
  #print('images ',len(d['all_events']['images']),'labels ',len(d['all_events']['labels']),'weights ',len(d['all_events']['weights']))

#print(str(d.keys()))
#if (
#for i in str(d.keys):
 # print(i)

#d['all_event'].keys()

#new


