# CSC 482 - Lab0x02
### Implementation and analysis of sorting algorithms

Sample output with MAX_RUN_TIME = .25s:

```
Generating list of length 1000, key width of 16
Sorting with BUBBLE SORT
Verifying... Sorted!

Generating list of length 1000, key width of 16
Sorting with SELECTION SORT
Verifying... Sorted!

Generating list of length 1000, key width of 16
Sorting with INSERTION SORT
Verifying... Sorted!

Generating list of length 1000, key width of 16
Sorting with RADIX SORT
Verifying... Sorted!

Generating list of length 1000, key width of 16
Sorting with COUNTING SORT
Verifying... Sorted!

Generating list of length 1000, key width of 16
Sorting with MERGE SORT
Verifying... Sorted!

Generating list of length 1000, key width of 16
Sorting with QUICKSORT
Verifying... Sorted!

Results for radix_sort
                           k=6                          k=12                          k=24                          k=48
              N           Time             DR           Time             DR           Time             DR           Time             DR      Predicted

              1         569158             na         398708             na         791397             na        1667239             na             na
              2         211358          0.371         404094           1.01         890322           1.13        1604595          0.962            2.0
              4         214123           1.01         416248           1.03        1668622           1.87        3758341           2.34            2.0
              8         229014           1.07         442174           1.06        1004275          0.602        1789286          0.476            2.0
             16         259576           1.13         489618           1.11        1065808           1.06        2895641           1.62            2.0
             32         731393           2.82         728462           1.49        1239242           1.16        2672441          0.923            2.0
             64         396578          0.542         773359           1.06        1642334           1.33        3902097           1.46            2.0
            128         646759           1.63        1163415            1.5        2361901           1.44        5064726            1.3            2.0
            256        1044673           1.62        1964881           1.69        3988140           1.69       11391168           2.25            2.0
            512        2176199           2.08        4829987           2.46        8708303           2.18       26624017           2.34            2.0
           1024        4407447           2.03        7132521           1.48       14541244           1.67       30321000           1.14            2.0
           2048        6822194           1.55       13536280            1.9       27347133           1.88       54409006           1.79            2.0
           4096       14063415           2.06       28464491            2.1       56712533           2.07      112444255           2.07            2.0
           8192       28820992           2.05       54378655           1.91      108920035           1.92      238468728           2.12            2.0
          16384       66474859           2.31      122368708           2.25      241710469           2.22      598361538           2.51            2.0
          32768      214708053           3.23      307441097           2.51      694045827           2.87             na             na            2.0
          65536      755908862           3.52             na             na             na             na             na             na            2.0

Results for quicksort
                           k=6                          k=12                          k=24                          k=48
              N           Time             DR           Time             DR           Time             DR           Time             DR      Predicted

              1        9513818             na           7598             na           1161             na           1012             na             na
              2          11783        0.00124           4254           0.56         303433       2.61e+02           5178           5.12            nan
              4           8653          0.734          14542           3.42           4482         0.0148           5235           1.01            4.0
              8          11335           1.31           8678          0.597          10212           2.28           9883           1.89            3.0
             16          22285           1.97          23400            2.7          20640           2.02          23496           2.38           2.67
             32          58230           2.61          42077            1.8          48919           2.37          49769           2.12            2.5
             64         105524           1.81         104621           2.49         123536           2.53         100317           2.02            2.4
            128         239267           2.27         356755           3.41         293267           2.37         234750           2.34           2.33
            256         567042           2.37         542898           1.52         896990           3.06         574961           2.45           2.29
            512        1286600           2.27        1264018           2.33        1468312           1.64        1550456            2.7           2.25
           1024        2966176           2.31        3520243           2.78        3118540           2.12        3084465           1.99           2.22
           2048        7524584           2.54        7453242           2.12        6723310           2.16        6548152           2.12            2.2
           4096       15747807           2.09       14887187            2.0       15483787            2.3       14783507           2.26           2.18
           8192       35655212           2.26       32731937            2.2       34031150            2.2       32016968           2.17           2.17
          16384       67217085           1.89       73882995           2.26       65254715           1.92       90469464           2.83           2.15
          32768      148219898           2.21      149153990           2.02      156688428            2.4      158793540           1.76           2.14
          65536      315608174           2.13      310489439           2.08      344236000            2.2      338372181           2.13           2.13

Results for merge_sort
                           k=6                          k=12                          k=24                          k=48
              N           Time             DR           Time             DR           Time             DR           Time             DR      Predicted

              1       12683121             na           9214             na           1818             na           1685             na             na
              2          10807       0.000852           3995          0.434           3355           1.85           3325           1.97            nan
              4          22974           2.13          13087           3.28          12865           3.83          12367           3.72            4.0
              8          32164            1.4          27732           2.12          24167           1.88          15829           1.28            3.0
             16          83655            2.6          76893           2.77          74002           3.06          65201           4.12           2.67
             32         101838           1.22         171750           2.23         173775           2.35         181281           2.78            2.5
             64         235876           2.32         213417           1.24         213852           1.23         228607           1.26            2.4
            128         573301           2.43         517078           2.42         487084           2.28         479140            2.1           2.33
            256        5565106           9.71        3658158           7.07        2881259           5.92        2886737           6.02           2.29
            512        2848486          0.512        2505694          0.685        2391865           0.83        2843070          0.985           2.25
           1024        5048697           1.77        5056382           2.02        5132156           2.15        5155903           1.81           2.22
           2048       11188186           2.22       11140515            2.2       11229168           2.19       11573159           2.24            2.2
           4096       25127223           2.25       25216244           2.26       25226567           2.25       25478010            2.2           2.18
           8192       56480212           2.25       56225926           2.23       66747013           2.65       57282563           2.25           2.17
          16384      137087602           2.43      139953411           2.49      138736300           2.08      138023172           2.41           2.15
          32768      371160063           2.71      366322240           2.62      369695181           2.66      374719041           2.71           2.14

Results for insertion_sort
                           k=6                          k=12                          k=24                          k=48
              N           Time             DR           Time             DR           Time             DR           Time             DR      Predicted

              1        4514178             na          36207             na          15461             na           2071             na             na
              2           6134        0.00136          22293          0.616           2522          0.163          20233           9.77            4.0
              4           6407           1.04           2670           0.12           2224          0.882           2679          0.132            4.0
              8          14030           2.19           9442           3.54           6419           2.89           6817           2.54            4.0
             16          72248           5.15          51107           5.41          50171           7.82          85217           12.5            4.0
             32          85768           1.19         116360           2.28          76638           1.53          77174          0.906            4.0
             64         331563           3.87         363278           3.12         341678           4.46         384594           4.98            4.0
            128        1059404            3.2        1125619            3.1        1337094           3.91        1279200           3.33            4.0
            256        5494691           5.19        5437151           4.83        5673906           4.24        6132342           4.79            4.0
            512       23932244           4.36       23150275           4.26       23686403           4.17       23806000           3.88            4.0
           1024      105119598           4.39      113960010           4.92      110238347           4.65      101943024           4.28            4.0
           2048      447728558           4.26      448294623           3.93      431857999           3.92      444694785           4.36            4.0

Results for bubble_sort
                           k=6                          k=12                          k=24                          k=48
              N           Time             DR           Time             DR           Time             DR           Time             DR      Predicted

              1         126612             na           2180             na           1155             na           1179             na             na
              2           5073         0.0401           3218           1.48           3223           2.79           1699           1.44            4.0
              4           8170           1.61           3707           1.15           4240           1.32           5823           3.43            4.0
              8          16294           1.99          16296            4.4          13645           3.22          10889           1.87            4.0
             16          51582           3.17          46882           2.88          50793           3.72          39402           3.62            4.0
             32         152895           2.96          96567           2.06         114946           2.26         153763            3.9            4.0
             64         389349           2.55         450109           4.66         403529           3.51         407515           2.65            4.0
            128        1688236           4.34        1476612           3.28        1483135           3.68        1621061           3.98            4.0
            256        6307138           3.74        7001765           4.74        8970193           6.05        6388003           3.94            4.0
            512       27012450           4.28       26963423           3.85       27640485           3.08       26482258           4.15            4.0
           1024      129470456           4.79      117709868           4.37      131632111           4.76      118618000           4.48            4.0
           2048      505719676           3.91      518870833           4.41      499651820            3.8      506241536           4.27            4.0
```

