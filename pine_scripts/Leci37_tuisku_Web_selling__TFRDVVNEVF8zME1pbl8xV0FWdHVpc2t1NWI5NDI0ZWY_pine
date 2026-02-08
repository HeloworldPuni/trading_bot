//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: LTCUSDT_30Min_1WAV_5b9424ef Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_LTCUSDT_30Min_1WAV_5b9424ef", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_LTCUSDT_30Min_5b9424ef(d, esa, d_tci, ci_wt2, wt2, ci, ap, tci)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ci <= 54.7514 )
		if( d <= 0.683458 )
			if( ap <= 62.5593 )
				if( ci_wt2 <= -5.37294 )
					if( wt2 <= 39.8517 )
						if( tci <= 32.3598 )
							if( ci_wt2 <= -46.5077 )
								if( ci <= -22.6714 )
									ret := 0.155015
								if( ci > -22.6714 )
									ret := 0.611940
							if( ci_wt2 > -46.5077 )
								if( tci <= -39.5504 )
									ret := 0.224000
								if( tci > -39.5504 )
									ret := 0.029252
						if( tci > 32.3598 )
							if( d <= 0.176184 )
								if( d <= 0.162708 )
									ret := 0.204082
								if( d > 0.162708 )
									ret := -0.625000
							if( d > 0.176184 )
								if( ap <= 61.6083 )
									ret := 0.623762
								if( ap > 61.6083 )
									ret := -0.222222
					if( wt2 > 39.8517 )
						if( wt2 <= 50.5263 )
							if( ap <= 51.6701 )
								if( ap <= 51.4821 )
									ret := 0.198276
								if( ap > 51.4821 )
									ret := 1.000000 // buy
							if( ap > 51.6701 )
								if( esa <= 62.0561 )
									ret := -0.199430
								if( esa > 62.0561 )
									ret := 0.500000
						if( wt2 > 50.5263 )
							if( ci_wt2 <= -28.7576 )
								if( d <= 0.393383 )
									ret := -0.079812
								if( d > 0.393383 )
									ret := 0.303571
							if( ci_wt2 > -28.7576 )
								if( esa <= 57.1058 )
									ret := 0.452555
								if( esa > 57.1058 )
									ret := 0.078652
				if( ci_wt2 > -5.37294 )
					if( wt2 <= 20.5453 )
						if( d <= 0.128086 )
							if( ci <= 32.3397 )
								if( ci_wt2 <= -1.76449 )
									ret := 0.137931
								if( ci_wt2 > -1.76449 )
									ret := -0.168449
							if( ci > 32.3397 )
								if( ci_wt2 <= 30.4505 )
									ret := 0.454545
								if( ci_wt2 > 30.4505 )
									ret := 0.033113
						if( d > 0.128086 )
							if( ap <= 61.7914 )
								if( wt2 <= -72.7985 )
									ret := 0.750000 // buy
								if( wt2 > -72.7985 )
									ret := 0.080054
							if( ap > 61.7914 )
								if( d_tci <= 61.23 )
									ret := 0.364238
								if( d_tci > 61.23 )
									ret := -0.222222
					if( wt2 > 20.5453 )
						if( tci <= 23.4215 )
							if( ci_wt2 <= 27.3104 )
								if( d <= 0.09537 )
									ret := 0.000000
								if( d > 0.09537 )
									ret := -0.714286 // sell
							if( ci_wt2 > 27.3104 )
								ret := 0.250000
						if( tci > 23.4215 )
							if( ci_wt2 <= 14.3181 )
								if( ci_wt2 <= 0.150602 )
									ret := -0.244898
								if( ci_wt2 > 0.150602 )
									ret := 0.108333
							if( ci_wt2 > 14.3181 )
								if( wt2 <= 22.7635 )
									ret := 0.280000
								if( wt2 > 22.7635 )
									ret := -0.375000
			if( ap > 62.5593 )
				if( d <= 0.310902 )
					if( ci <= -49.1829 )
						if( esa <= 69.5732 )
							if( d_tci <= -39.3295 )
								if( wt2 <= 57.3549 )
									ret := -0.842105 // sell
								if( wt2 > 57.3549 )
									ret := 0.000000
							if( d_tci > -39.3295 )
								if( tci <= -24.877 )
									ret := -0.053416
								if( tci > -24.877 )
									ret := 0.101197
						if( esa > 69.5732 )
							if( wt2 <= -40.8818 )
								if( ci_wt2 <= -23.4847 )
									ret := 0.152632
								if( ci_wt2 > -23.4847 )
									ret := -0.169811
							if( wt2 > -40.8818 )
								if( d <= 0.095 )
									ret := 0.029412
								if( d > 0.095 )
									ret := -0.123870
					if( ci > -49.1829 )
						if( ci <= -46.127 )
							if( ci_wt2 <= -89.6461 )
								if( tci <= 36.9411 )
									ret := -1.000000 // sell
								if( tci > 36.9411 )
									ret := 0.400000
							if( ci_wt2 > -89.6461 )
								if( d <= 0.227743 )
									ret := 0.107477
								if( d > 0.227743 )
									ret := 0.388889
						if( ci > -46.127 )
							if( d <= 0.162397 )
								if( ci <= -41.2018 )
									ret := -0.184049
								if( ci > -41.2018 )
									ret := -0.023922
							if( d > 0.162397 )
								if( wt2 <= 58.1794 )
									ret := 0.033689
								if( wt2 > 58.1794 )
									ret := -0.179487
				if( d > 0.310902 )
					if( ci <= -78.4861 )
						if( ci_wt2 <= -90.1675 )
							if( ap <= 95.9853 )
								if( ap <= 70.4603 )
									ret := -0.027586
								if( ap > 70.4603 )
									ret := 0.256813
							if( ap > 95.9853 )
								if( esa <= 113.565 )
									ret := -0.227425
								if( esa > 113.565 )
									ret := 0.044266
						if( ci_wt2 > -90.1675 )
							if( tci <= -59.471 )
								if( ap <= 88.5967 )
									ret := 0.088670
								if( ap > 88.5967 )
									ret := -0.428571
							if( tci > -59.471 )
								if( ap <= 95.6407 )
									ret := 0.345238
								if( ap > 95.6407 )
									ret := 0.090909
					if( ci > -78.4861 )
						if( wt2 <= -55.0656 )
							if( esa <= 107.912 )
								if( ci_wt2 <= 1.88706 )
									ret := -0.308219
								if( ci_wt2 > 1.88706 )
									ret := -0.027523
							if( esa > 107.912 )
								if( ci_wt2 <= 39.2419 )
									ret := -0.950000 // sell
								if( ci_wt2 > 39.2419 )
									ret := -0.545455
						if( wt2 > -55.0656 )
							if( wt2 <= 4.32439 )
								if( wt2 <= -11.5269 )
									ret := 0.050402
								if( wt2 > -11.5269 )
									ret := 0.186971
							if( wt2 > 4.32439 )
								if( tci <= 8.43212 )
									ret := -0.156897
								if( tci > 8.43212 )
									ret := 0.011887
		if( d > 0.683458 )
			if( ci <= -112.611 )
				if( ci <= -162.649 )
					if( wt2 <= -53.2714 )
						if( esa <= 93.755 )
							if( tci <= -69.4859 )
								if( ap <= 84.0176 )
									ret := -0.200000
								if( ap > 84.0176 )
									ret := 0.800000 // buy
							if( tci > -69.4859 )
								ret := 1.000000 // buy
						if( esa > 93.755 )
							if( tci <= -83.3182 )
								ret := 1.000000 // buy
							if( tci > -83.3182 )
								if( esa <= 106.783 )
									ret := -1.000000 // sell
								if( esa > 106.783 )
									ret := -0.315789
					if( wt2 > -53.2714 )
						if( tci <= -49.8893 )
							if( esa <= 66.1274 )
								if( d_tci <= 59.4772 )
									ret := 0.500000
								if( d_tci > 59.4772 )
									ret := -1.000000 // sell
							if( esa > 66.1274 )
								if( esa <= 172.325 )
									ret := 0.696970
								if( esa > 172.325 )
									ret := 0.976190 // buy
						if( tci > -49.8893 )
							if( ap <= 90.4937 )
								if( d <= 0.827763 )
									ret := 0.478261
								if( d > 0.827763 )
									ret := 0.970588 // buy
							if( ap > 90.4937 )
								if( ci_wt2 <= -191.343 )
									ret := -0.142857
								if( ci_wt2 > -191.343 )
									ret := 0.482014
				if( ci > -162.649 )
					if( ci_wt2 <= -174.632 )
						if( ci_wt2 <= -179.028 )
							if( ap <= 120.751 )
								if( ap <= 104.819 )
									ret := 0.500000
								if( ap > 104.819 )
									ret := -1.000000 // sell
							if( ap > 120.751 )
								if( esa <= 153.493 )
									ret := 0.909091 // buy
								if( esa > 153.493 )
									ret := -0.142857
						if( ci_wt2 > -179.028 )
							if( esa <= 151.2 )
								ret := -1.000000 // sell
							if( esa > 151.2 )
								if( esa <= 182.008 )
									ret := 0.250000
								if( esa > 182.008 )
									ret := -0.888889 // sell
					if( ci_wt2 > -174.632 )
						if( d <= 1.89161 )
							if( d_tci <= -16.6683 )
								if( ap <= 181.905 )
									ret := 0.827586 // buy
								if( ap > 181.905 )
									ret := 0.500000
							if( d_tci > -16.6683 )
								if( d_tci <= -7.79151 )
									ret := -0.341463
								if( d_tci > -7.79151 )
									ret := 0.279341
						if( d > 1.89161 )
							if( ci_wt2 <= -127.173 )
								if( esa <= 315.878 )
									ret := 0.305263
								if( esa > 315.878 )
									ret := 0.950000 // buy
							if( ci_wt2 > -127.173 )
								if( tci <= -69.7943 )
									ret := 0.472222
								if( tci > -69.7943 )
									ret := -0.055710
			if( ci > -112.611 )
				if( ap <= 367.578 )
					if( wt2 <= 54.3746 )
						if( esa <= 247.2 )
							if( ci <= -52.6214 )
								if( esa <= 215.398 )
									ret := 0.114718
								if( esa > 215.398 )
									ret := 0.387712
							if( ci > -52.6214 )
								if( esa <= 180.894 )
									ret := 0.086442
								if( esa > 180.894 )
									ret := -0.040169
						if( esa > 247.2 )
							if( esa <= 254.454 )
								if( tci <= -45.8861 )
									ret := 0.205128
								if( tci > -45.8861 )
									ret := 0.698324
							if( esa > 254.454 )
								if( ci_wt2 <= -100.971 )
									ret := -0.401786
								if( ci_wt2 > -100.971 )
									ret := 0.161475
					if( wt2 > 54.3746 )
						if( esa <= 151.917 )
							if( d <= 1.38805 )
								if( ap <= 128.396 )
									ret := 0.048913
								if( ap > 128.396 )
									ret := -0.397959
							if( d > 1.38805 )
								if( ap <= 80.3969 )
									ret := -0.620690
								if( ap > 80.3969 )
									ret := 0.401674
						if( esa > 151.917 )
							if( ap <= 170.148 )
								if( ci <= 46.1982 )
									ret := 0.687500
								if( ci > 46.1982 )
									ret := 0.086957
							if( ap > 170.148 )
								if( esa <= 175.633 )
									ret := -0.142857
								if( esa > 175.633 )
									ret := 0.399023
				if( ap > 367.578 )
					if( ci <= -96.2512 )
						ret := 0.500000
					if( ci > -96.2512 )
						if( esa <= 370.862 )
							if( d <= 3.05361 )
								ret := 1.000000 // buy
							if( d > 3.05361 )
								ret := -0.400000
						if( esa > 370.862 )
							if( ci <= 33.4418 )
								if( wt2 <= -17.9469 )
									ret := -0.650000
								if( wt2 > -17.9469 )
									ret := -0.907407 // sell
							if( ci > 33.4418 )
								if( tci <= 57.1584 )
									ret := 0.250000
								if( tci > 57.1584 )
									ret := -0.600000
	if( ci > 54.7514 )
		if( ap <= 181.849 )
			if( d_tci <= 30.4475 )
				if( ci <= 86.1779 )
					if( esa <= 84.9769 )
						if( d <= 2.43196 )
							if( tci <= 24.8019 )
								if( wt2 <= 16.6682 )
									ret := 0.038038
								if( wt2 > 16.6682 )
									ret := 0.368421
							if( tci > 24.8019 )
								if( d <= 0.577641 )
									ret := -0.049484
								if( d > 0.577641 )
									ret := 0.095372
						if( d > 2.43196 )
							ret := -1.000000 // sell
					if( esa > 84.9769 )
						if( d <= 1.84297 )
							if( d_tci <= 0.460266 )
								if( tci <= 20.578 )
									ret := 0.088825
								if( tci > 20.578 )
									ret := -0.135281
							if( d_tci > 0.460266 )
								if( esa <= 151.144 )
									ret := -0.131034
								if( esa > 151.144 )
									ret := -0.377273
						if( d > 1.84297 )
							if( d_tci <= -11.9148 )
								if( esa <= 170.509 )
									ret := 0.128440
								if( esa > 170.509 )
									ret := 0.566667
							if( d_tci > -11.9148 )
								if( ap <= 154.869 )
									ret := -0.709677 // sell
								if( ap > 154.869 )
									ret := -0.019231
				if( ci > 86.1779 )
					if( ap <= 84.4267 )
						if( wt2 <= 54.8583 )
							if( ci <= 139.813 )
								if( ap <= 51.0629 )
									ret := 0.241722
								if( ap > 51.0629 )
									ret := 0.019989
							if( ci > 139.813 )
								if( ci <= 151.027 )
									ret := -0.303797
								if( ci > 151.027 )
									ret := -0.020734
						if( wt2 > 54.8583 )
							if( d <= 1.25662 )
								if( d <= 0.709548 )
									ret := -0.100592
								if( d > 0.709548 )
									ret := -0.497076
							if( d > 1.25662 )
								if( d_tci <= -79.0804 )
									ret := -0.333333
								if( d_tci > -79.0804 )
									ret := 0.540541
					if( ap > 84.4267 )
						if( d <= 2.21946 )
							if( ci <= 97.8487 )
								if( tci <= 68.064 )
									ret := 0.250426
								if( tci > 68.064 )
									ret := 0.561798
							if( ci > 97.8487 )
								if( d_tci <= -69.1624 )
									ret := 0.440945
								if( d_tci > -69.1624 )
									ret := 0.032288
						if( d > 2.21946 )
							if( tci <= 34.8291 )
								if( ap <= 167.36 )
									ret := -0.350000
								if( ap > 167.36 )
									ret := 0.709091 // buy
							if( tci > 34.8291 )
								if( ci_wt2 <= 60.1031 )
									ret := -0.311927
								if( ci_wt2 > 60.1031 )
									ret := -0.626667
			if( d_tci > 30.4475 )
				if( ci_wt2 <= 162.852 )
					if( d <= 0.38368 )
						if( ci_wt2 <= 143.562 )
							if( ci_wt2 <= 109.599 )
								if( esa <= 51.9526 )
									ret := -0.600000
								if( esa > 51.9526 )
									ret := -0.073171
							if( ci_wt2 > 109.599 )
								if( tci <= -43.2366 )
									ret := 0.785714 // buy
								if( tci > -43.2366 )
									ret := 0.232558
						if( ci_wt2 > 143.562 )
							if( d <= 0.301138 )
								ret := 0.166667
							if( d > 0.301138 )
								if( ap <= 82.678 )
									ret := -0.941176 // sell
								if( ap > 82.678 )
									ret := -0.250000
					if( d > 0.38368 )
						if( ap <= 103.421 )
							if( ap <= 83.9417 )
								if( esa <= 79.7413 )
									ret := 0.532258
								if( esa > 79.7413 )
									ret := -0.750000 // sell
							if( ap > 83.9417 )
								if( wt2 <= -45.5515 )
									ret := 0.914286 // buy
								if( wt2 > -45.5515 )
									ret := 0.454545
						if( ap > 103.421 )
							if( esa <= 125.254 )
								if( d <= 0.875237 )
									ret := 0.222222
								if( d > 0.875237 )
									ret := -1.000000 // sell
							if( esa > 125.254 )
								if( wt2 <= -60.7838 )
									ret := -1.000000 // sell
								if( wt2 > -60.7838 )
									ret := 0.434343
				if( ci_wt2 > 162.852 )
					if( d <= 0.287559 )
						ret := 0.200000
					if( d > 0.287559 )
						if( ap <= 84.7417 )
							if( ci_wt2 <= 188.381 )
								ret := 1.000000 // buy
							if( ci_wt2 > 188.381 )
								ret := 0.750000 // buy
						if( ap > 84.7417 )
							ret := 0.333333
		if( ap > 181.849 )
			if( tci <= 75.9315 )
				if( tci <= 57.1836 )
					if( d_tci <= -17.5906 )
						if( ap <= 185.174 )
							if( d_tci <= -25.5917 )
								if( ci_wt2 <= 34.0623 )
									ret := -0.750000 // sell
								if( ci_wt2 > 34.0623 )
									ret := -0.293651
							if( d_tci > -25.5917 )
								if( tci <= 20.8942 )
									ret := -0.666667
								if( tci > 20.8942 )
									ret := 0.319149
						if( ap > 185.174 )
							if( esa <= 360.539 )
								if( ci <= 81.6228 )
									ret := 0.142857
								if( ci > 81.6228 )
									ret := -0.071090
							if( esa > 360.539 )
								if( wt2 <= 42.4218 )
									ret := 0.950000 // buy
								if( wt2 > 42.4218 )
									ret := 0.250000
					if( d_tci > -17.5906 )
						if( wt2 <= 10.2232 )
							if( esa <= 284.953 )
								if( esa <= 271.252 )
									ret := -0.171840
								if( esa > 271.252 )
									ret := 0.583333
							if( esa > 284.953 )
								if( ap <= 325.875 )
									ret := -0.921569 // sell
								if( ap > 325.875 )
									ret := -0.214286
						if( wt2 > 10.2232 )
							if( ci <= 90.8255 )
								if( d_tci <= -16.6256 )
									ret := -0.555556
								if( d_tci > -16.6256 )
									ret := -0.976190 // sell
							if( ci > 90.8255 )
								if( ci_wt2 <= 94.5864 )
									ret := 0.666667
								if( ci_wt2 > 94.5864 )
									ret := -1.000000 // sell
				if( tci > 57.1836 )
					if( esa <= 201.253 )
						if( esa <= 185.429 )
							if( d <= 0.837679 )
								ret := 0.750000 // buy
							if( d > 0.837679 )
								if( ci <= 84.0735 )
									ret := -0.307692
								if( ci > 84.0735 )
									ret := -0.852941 // sell
						if( esa > 185.429 )
							if( d <= 2.97271 )
								if( ci_wt2 <= 15.3994 )
									ret := -0.500000
								if( ci_wt2 > 15.3994 )
									ret := 0.362069
							if( d > 2.97271 )
								if( esa <= 187.783 )
									ret := 0.000000
								if( esa > 187.783 )
									ret := 0.760000 // buy
					if( esa > 201.253 )
						if( tci <= 66.7661 )
							if( d <= 1.76126 )
								if( ap <= 207.9 )
									ret := -0.636364
								if( ap > 207.9 )
									ret := 0.047619
							if( d > 1.76126 )
								if( ci <= 137.467 )
									ret := -0.785714 // sell
								if( ci > 137.467 )
									ret := -0.166667
						if( tci > 66.7661 )
							if( ci <= 120.721 )
								if( ci_wt2 <= 47.4059 )
									ret := -0.018182
								if( ci_wt2 > 47.4059 )
									ret := -0.750000 // sell
							if( ci > 120.721 )
								if( wt2 <= 58.8975 )
									ret := 0.400000
								if( wt2 > 58.8975 )
									ret := 1.000000 // buy
			if( tci > 75.9315 )
				if( ci <= 71.45 )
					if( ap <= 246.874 )
						if( d <= 5.36884 )
							ret := -0.750000 // sell
						if( d > 5.36884 )
							ret := -0.400000
					if( ap > 246.874 )
						ret := 0.833333 // buy
				if( ci > 71.45 )
					if( ci <= 91.0913 )
						if( wt2 <= 77.7523 )
							if( ci_wt2 <= 12.0698 )
								ret := 1.000000 // buy
							if( ci_wt2 > 12.0698 )
								ret := 0.500000
						if( wt2 > 77.7523 )
							ret := -0.166667
					if( ci > 91.0913 )
						if( d <= 2.27808 )
							ret := 0.500000
						if( d > 2.27808 )
							if( wt2 <= 69.8982 )
								ret := 0.750000 // buy
							if( wt2 > 69.8982 )
								if( ap <= 197.689 )
									ret := 0.750000 // buy
								if( ap > 197.689 )
									ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Wave_Trend_Calculation 
//@version=5
//indicator "WaveTrend [LazyBear]", shorttitle="WT_LB", overlay=false)

n1 = input.int(10, title="Channel Length")
n2 = input.int(21, title="Average Length")
obLevel1 = input.float(60, title="Over Bought Level 1")
obLevel2 = input.float(53, title="Over Bought Level 2")
osLevel1 = input.float(-60, title="Over Sold Level 1")
osLevel2 = input.float(-53, title="Over Sold Level 2")

ap = hlc3
esa = ta.ema(ap, n1)
d = ta.ema(math.abs(ap - esa), n1)
ci = (ap - esa) / (0.015 * d)
tci = ta.ema(ci, n2)

wt1 = tci
wt2 = ta.sma(wt1, 4)

d_tci = d-tci
ci_wt2 = ci - wt2

plot(0, color=color.gray)
plot(obLevel1, color=color.red)
plot(osLevel1, color=color.green)
plot(obLevel2, color=color.red, linewidth=2, style=plot.style_line, title="OB Level 2 (Dashed)", color=color.red)
plot(osLevel2, color=color.green, linewidth=2, style=plot.style_line, title="OS Level 2 (Dashed)", color=color.green)

plot(wt1, color=color.green, title="WT1")
plot(wt2, color=color.red, title="WT2", style=plot.style_line, linewidth=1)
plot(wt1 - wt2, color=color.new(color.blue, 80), title="WT1-WT2", style=plot.style_area)

// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_LTCUSDT_30Min_5b9424ef(d, esa, d_tci, ci_wt2, wt2, ci, ap, tci)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.


