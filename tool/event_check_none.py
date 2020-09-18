import h5py

data=[
['new=qcd1000to1500_1.h5 old=data_1.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 42, 'none', 'none', 'none', 43], [43, 98, 985, 1028, 1083, 56], [99, 1126, -99, 0, 1027, 1028], [1127, 1226, 775, 1902, 2001, 100], [1227, 2044, -143, 1084, 1901, 818], [2045, 2137, 886, 2931, 3023, 93], [2138, 3066, -136, 2002, 2930, 929], [3067, 3167, 571, 3638, 3738, 101], [3168, 3781, -144, 3024, 3637, 614], [3782, 3855, 'none', 'none', 'none', 74], [3856, 4095, -117, 3739, 3978, 240], 
['new=qcd1000to1500_2.h5 old=data_2.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 116, 'none', 'none', 'none', 117], [117, 369, -117, 0, 252, 253], [370, 478, 833, 1203, 1311, 109], [479, 1354, -152, 327, 1202, 876], [1355, 1459, 618, 1973, 2077, 105], [1460, 2120, -148, 1312, 1972, 661], [2121, 2198, 1008, 3129, 3206, 78], [2199, 3249, -121, 2078, 3128, 1051], [3250, 3350, 'none', 'none', 'none', 101], [3351, 4095, -144, 3207, 3951, 745], 
['new=qcd1000to1500_3.h5 old=data_3.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 143, 'none', 'none', 'none', 144], [144, 172, -144, 0, 28, 29], [173, 202, 932, 1105, 1134, 30], [203, 1177, -73, 130, 1104, 975], [1178, 1280, 1007, 2185, 2287, 103], [1281, 1396, 0, 1281, 1396, 116], [1397, 1499, -219, 1178, 1280, 103], [1500, 2287, -103, 1397, 2184, 788], [2288, 2302, 854, 3142, 3156, 15], [2303, 3156, -15, 2288, 3141, 854], [3157, 3243, 'none', 'none', 'none', 87], [3244, 4095, -87, 3157, 4008, 852], 
['new=qcd1000to1500_4.h5 old=data_4.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 86, 'none', 'none', 'none', 87], [87, 98, -87, 0, 11, 12], [99, 187, 809, 908, 996, 89], [188, 996, -89, 99, 907, 809], [997, 1098, 884, 1881, 1982, 102], [1099, 1982, -102, 997, 1880, 884], [1983, 2045, 912, 2895, 2957, 63], [2046, 2957, -63, 1983, 2894, 912], [2958, 3064, 729, 3687, 3793, 107], [3065, 3793, -107, 2958, 3686, 729], [3794, 3855, 'none', 'none', 'none', 62], [3856, 4095, -62, 3794, 4033, 240], 
['new=qcd1000to1500_5.h5 old=data_5.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 61, 'none', 'none', 'none', 62], [62, 667, -62, 0, 605, 606], [668, 4095, 0, 668, 4095, 3428]]

#########################
data_none=[
           ['new=qcd1000to1500_1.h5 old=data_3.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 42, 1135, 1135, 1177, 43],
           ['new=qcd1000to1500_1.h5 old=data_2.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [3782, 3855, -3529, 253, 326, 74], 
           
           ['new=qcd1000to1500_2.h5 old=data_1.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 116, 3979, 3979, 4095, 117],#1full
           ['new=qcd1000to1500_2.h5 old=data_3.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [3250, 3350, -3221, 29, 129, 101],#3full
           
           ['new=qcd1000to1500_3.h5 old=data_2.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 143, 3952, 3952, 4095, 144],
           ['new=qcd1000to1500_3.h5 old=data_4.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [3157, 3243, -3145, 12, 98, 87],
           
           ['new=qcd1000to1500_4.h5 old=data_3.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 86, 4009, 4009, 4095, 87],
           ['new=qcd1000to1500_4.h5 old=data_5.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [3794, 3855, -3188, 606, 667, 62],
            
           ['new=qcd1000to1500_5.h5 old=data_4.h5'], ['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'], [0, 61, 4034, 4034, 4095, 62]
          ]
#########################################################3
#for k in range(1,6)
'''
difference=[]

predict=[(3, 4, 3157, 3243), (4, 5, 3794, 3855)]
for k in predict:
  new=h5py.File('/home/swkim/test_preprocess_new/trackpt_hdf5_32PU_224x224/QCDBkg/HT1000to1500/qcd1000to1500_'+str(k[0])+'.h5','r')
  old=h5py.File('/data/swkim/trackPt_nchw/hdf5_32PU_224x224/QCDBkg/HT1000to1500/data_'+str(k[1])+'.h5','r')
  
  difference.append(['new=qcd1000to1500_'+str(k[0])+'.h5 old='+'data_'+str(k[1])+'.h5'])
  difference.append(['new_start', 'new_end', 'old-new', 'old_start', 'old_end', 'how_many'])
  
  new_images=new['all_events']['images']
  old_images=old['all_events']['images']
  
  
  temp_diff=[0,0,0,0,0,0]
  
  i=k[2]
  
  while(i<k[3]+1):
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
        while( i+1<(k[3]+1) and (new_images[i+1,0,:,:]==old_images[i+1+diff,0,:,:]).all()):
          i=i+1
          print('new=',i,'old=',i+diff)
        temp_diff[1]=i
        temp_diff[3]=temp_diff[0]+temp_diff[2]
        temp_diff[4]=temp_diff[1]+temp_diff[2]
        temp_diff[5]=temp_diff[1]-temp_diff[0]+1
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
          temp_diff[3]='none'
          temp_diff[4]='none'
        temp_diff[5]=temp_diff[1]-temp_diff[0]+1
        print('new=',i,'old=none')
        
    i=i+1
'''

for i in data_none:
  try:
    print('{0:>10}{1:>10}{2:>10}{3:>10}{4:>10}{5:>10}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
  except:
    print('{0:>10}'.format(i[0]))
  
  
  
  
