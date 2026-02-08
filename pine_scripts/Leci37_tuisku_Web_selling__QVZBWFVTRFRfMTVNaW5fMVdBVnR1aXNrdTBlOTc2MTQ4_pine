//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Wave_Trend_Calculation
// ID_model: AVAXUSDT_15Min_1WAV_0e976148 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AVAXUSDT_15Min_1WAV_0e976148", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AVAXUSDT_15Min_0e976148(tci, ci, d_tci, esa, d, ci_wt2, wt2, ap)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( d_tci <= 57.9027 )
		if( ci_wt2 <= -37.7603 )
			if( wt2 <= 52.1609 )
				if( d <= 0.186479 )
					if( esa <= 29.2015 )
						if( ci <= -185.579 )
							if( ci <= -223.013 )
								if( ci_wt2 <= -234.226 )
									ret := 0.333333
								if( ci_wt2 > -234.226 )
									ret := -0.600000
							if( ci > -223.013 )
								if( d <= 0.038648 )
									ret := 0.000000
								if( d > 0.038648 )
									ret := 0.528302
						if( ci > -185.579 )
							if( d <= 0.029207 )
								if( d_tci <= 20.9949 )
									ret := 0.004458
								if( d_tci > 20.9949 )
									ret := -0.060711
							if( d > 0.029207 )
								if( esa <= 17.3587 )
									ret := 0.115377
								if( esa > 17.3587 )
									ret := 0.052685
					if( esa > 29.2015 )
						if( tci <= -39.1225 )
							if( esa <= 46.1065 )
								if( esa <= 30.1275 )
									ret := -0.090909
								if( esa > 30.1275 )
									ret := 0.287234
							if( esa > 46.1065 )
								if( d_tci <= 44.1886 )
									ret := -0.714286 // sell
								if( d_tci > 44.1886 )
									ret := 0.000000
						if( tci > -39.1225 )
							if( ci_wt2 <= -195.77 )
								if( ci <= -203.101 )
									ret := 0.750000 // buy
								if( ci > -203.101 )
									ret := 1.000000 // buy
							if( ci_wt2 > -195.77 )
								if( ci <= -162.376 )
									ret := -0.481928
								if( ci > -162.376 )
									ret := -0.063634
				if( d > 0.186479 )
					if( d_tci <= 36.156 )
						if( esa <= 39.3791 )
							if( esa <= 36.1867 )
								if( d <= 0.492052 )
									ret := 0.088468
								if( d > 0.492052 )
									ret := -0.650000
							if( esa > 36.1867 )
								if( d <= 0.19973 )
									ret := 0.380000
								if( d > 0.19973 )
									ret := -0.312102
						if( esa > 39.3791 )
							if( ci_wt2 <= -54.0814 )
								if( ci_wt2 <= -139.566 )
									ret := 0.452174
								if( ci_wt2 > -139.566 )
									ret := 0.035593
							if( ci_wt2 > -54.0814 )
								if( ap <= 52.2903 )
									ret := 0.241071
								if( ap > 52.2903 )
									ret := 0.651786
					if( d_tci > 36.156 )
						if( ci <= -186.333 )
							if( wt2 <= -37.6561 )
								ret := 0.333333
							if( wt2 > -37.6561 )
								if( tci <= -41.5134 )
									ret := 1.000000 // buy
								if( tci > -41.5134 )
									ret := 0.500000
						if( ci > -186.333 )
							if( ci <= -145.627 )
								if( ci_wt2 <= -112.768 )
									ret := -0.024096
								if( ci_wt2 > -112.768 )
									ret := -0.857143 // sell
							if( ci > -145.627 )
								if( d <= 0.66812 )
									ret := 0.325371
								if( d > 0.66812 )
									ret := -0.211111
			if( wt2 > 52.1609 )
				if( wt2 <= 54.5428 )
					if( d <= 0.054129 )
						if( ci_wt2 <= -85.5286 )
							if( ap <= 13.9987 )
								ret := 0.000000
							if( ap > 13.9987 )
								if( esa <= 20.9949 )
									ret := -0.600000
								if( esa > 20.9949 )
									ret := 0.000000
						if( ci_wt2 > -85.5286 )
							if( ci <= -23.8919 )
								ret := 1.000000 // buy
							if( ci > -23.8919 )
								if( wt2 <= 52.8237 )
									ret := 0.400000
								if( wt2 > 52.8237 )
									ret := -0.034483
					if( d > 0.054129 )
						if( d_tci <= -49.6671 )
							if( wt2 <= 53.1732 )
								ret := 0.571429
							if( wt2 > 53.1732 )
								if( ci_wt2 <= -46.9444 )
									ret := 0.500000
								if( ci_wt2 > -46.9444 )
									ret := 1.000000 // buy
						if( d_tci > -49.6671 )
							if( esa <= 34.1144 )
								if( ap <= 31.0603 )
									ret := 0.391960
								if( ap > 31.0603 )
									ret := 1.000000 // buy
							if( esa > 34.1144 )
								if( tci <= 45.6347 )
									ret := 0.548387
								if( tci > 45.6347 )
									ret := -0.105263
				if( wt2 > 54.5428 )
					if( ap <= 43.1479 )
						if( d <= 0.227337 )
							if( d_tci <= -55.9228 )
								if( ap <= 27.2742 )
									ret := 0.305439
								if( ap > 27.2742 )
									ret := -0.077922
							if( d_tci > -55.9228 )
								if( ap <= 22.4315 )
									ret := 0.000000
								if( ap > 22.4315 )
									ret := 0.227437
						if( d > 0.227337 )
							if( ci <= 36.4251 )
								if( ci_wt2 <= -55.5326 )
									ret := 0.602151
								if( ci_wt2 > -55.5326 )
									ret := 0.310078
							if( ci > 36.4251 )
								if( esa <= 25.7544 )
									ret := -0.909091 // sell
								if( esa > 25.7544 )
									ret := 0.583333
					if( ap > 43.1479 )
						if( ci <= 17.1887 )
							if( d <= 0.947317 )
								if( ci <= -24.0134 )
									ret := 0.000000
								if( ci > -24.0134 )
									ret := -0.616438
							if( d > 0.947317 )
								ret := 0.400000
						if( ci > 17.1887 )
							if( wt2 <= 70.0244 )
								if( d_tci <= -62.821 )
									ret := 0.750000 // buy
								if( d_tci > -62.821 )
									ret := 1.000000 // buy
							if( wt2 > 70.0244 )
								ret := 0.000000
		if( ci_wt2 > -37.7603 )
			if( esa <= 57.9626 )
				if( ci <= 175.277 )
					if( d <= 0.568028 )
						if( d <= 0.096062 )
							if( ap <= 17.3688 )
								if( d <= 0.053451 )
									ret := 0.009197
								if( d > 0.053451 )
									ret := 0.114545
							if( ap > 17.3688 )
								if( ci_wt2 <= 173.81 )
									ret := -0.011597
								if( ci_wt2 > 173.81 )
									ret := -0.480000
						if( d > 0.096062 )
							if( ap <= 17.1091 )
								if( ci <= -36.4867 )
									ret := 0.311547
								if( ci > -36.4867 )
									ret := 0.107779
							if( ap > 17.1091 )
								if( tci <= 64.0847 )
									ret := 0.055708
								if( tci > 64.0847 )
									ret := -0.052576
					if( d > 0.568028 )
						if( ap <= 42.0399 )
							if( d_tci <= -79.1524 )
								if( wt2 <= 84.6546 )
									ret := -0.935484 // sell
								if( wt2 > 84.6546 )
									ret := -0.416667
							if( d_tci > -79.1524 )
								if( ci_wt2 <= 111.703 )
									ret := -0.263514
								if( ci_wt2 > 111.703 )
									ret := -0.862069 // sell
						if( ap > 42.0399 )
							if( tci <= 53.8634 )
								if( d_tci <= -27.6487 )
									ret := 0.602041
								if( d_tci > -27.6487 )
									ret := -0.090909
							if( tci > 53.8634 )
								if( ap <= 46.52 )
									ret := 0.333333
								if( ap > 46.52 )
									ret := -0.449153
				if( ci > 175.277 )
					if( ci_wt2 <= 211.021 )
						if( ci <= 190.928 )
							if( wt2 <= 47.2276 )
								if( ap <= 19.6344 )
									ret := 0.551181
								if( ap > 19.6344 )
									ret := 0.231481
							if( wt2 > 47.2276 )
								if( ap <= 22.5133 )
									ret := -0.583333
								if( ap > 22.5133 )
									ret := 0.818182 // buy
						if( ci > 190.928 )
							if( esa <= 15.5463 )
								if( d <= 0.053049 )
									ret := -0.181818
								if( d > 0.053049 )
									ret := 0.750000 // buy
							if( esa > 15.5463 )
								if( ci <= 206.71 )
									ret := -0.402439
								if( ci > 206.71 )
									ret := 0.285714
					if( ci_wt2 > 211.021 )
						if( d <= 0.061869 )
							if( ap <= 15.802 )
								if( wt2 <= -25.0553 )
									ret := 0.000000
								if( wt2 > -25.0553 )
									ret := -0.363636
							if( ap > 15.802 )
								if( ci_wt2 <= 221.278 )
									ret := 1.000000 // buy
								if( ci_wt2 > 221.278 )
									ret := 0.000000
						if( d > 0.061869 )
							if( d_tci <= 7.73514 )
								if( ap <= 21.5575 )
									ret := 0.965517 // buy
								if( ap > 21.5575 )
									ret := 0.600000
							if( d_tci > 7.73514 )
								ret := 0.250000
			if( esa > 57.9626 )
				if( tci <= 52.8738 )
					if( ci_wt2 <= 82.9095 )
						if( wt2 <= 42.651 )
							if( wt2 <= 24.8125 )
								if( d <= 0.331252 )
									ret := -0.129630
								if( d > 0.331252 )
									ret := -0.456954
							if( wt2 > 24.8125 )
								if( d <= 0.745669 )
									ret := -0.700787 // sell
								if( d > 0.745669 )
									ret := 0.200000
						if( wt2 > 42.651 )
							if( ci <= 10.5958 )
								ret := -0.600000
							if( ci > 10.5958 )
								if( d_tci <= -45.9376 )
									ret := 0.166667
								if( d_tci > -45.9376 )
									ret := 0.882353 // buy
					if( ci_wt2 > 82.9095 )
						if( ci <= 133.147 )
							if( d_tci <= 40.1991 )
								if( tci <= 29.2922 )
									ret := 0.192771
								if( tci > 29.2922 )
									ret := 0.750000 // buy
							if( d_tci > 40.1991 )
								if( d_tci <= 44.9471 )
									ret := -0.750000 // sell
								if( d_tci > 44.9471 )
									ret := -1.000000 // sell
						if( ci > 133.147 )
							if( esa <= 61.6692 )
								if( ap <= 61.37 )
									ret := -0.466667
								if( ap > 61.37 )
									ret := 1.000000 // buy
							if( esa > 61.6692 )
								if( ap <= 67.9167 )
									ret := -1.000000 // sell
								if( ap > 67.9167 )
									ret := -0.500000
				if( tci > 52.8738 )
					if( ci_wt2 <= 48.3881 )
						if( wt2 <= 68.2293 )
							if( wt2 <= 51.3915 )
								ret := -0.500000
							if( wt2 > 51.3915 )
								if( tci <= 56.2656 )
									ret := -1.000000 // sell
								if( tci > 56.2656 )
									ret := -0.840000 // sell
						if( wt2 > 68.2293 )
							ret := -0.250000
					if( ci_wt2 > 48.3881 )
						ret := 0.166667
	if( d_tci > 57.9027 )
		if( ci_wt2 <= 9.67812 )
			if( d <= 0.59572 )
				if( ap <= 55.2223 )
					if( d <= 0.057958 )
						if( ci <= -56.2899 )
							if( wt2 <= -58.5258 )
								if( ap <= 13.0995 )
									ret := 0.000000
								if( ap > 13.0995 )
									ret := -0.234234
							if( wt2 > -58.5258 )
								if( ci <= -203.765 )
									ret := 0.636364
								if( ci > -203.765 )
									ret := 0.091575
						if( ci > -56.2899 )
							if( ci <= -53.0315 )
								if( ci <= -55.5652 )
									ret := -0.400000
								if( ci > -55.5652 )
									ret := -0.923077 // sell
							if( ci > -53.0315 )
								if( esa <= 13.6181 )
									ret := 0.200000
								if( esa > 13.6181 )
									ret := -0.500000
					if( d > 0.057958 )
						if( ap <= 13.1004 )
							if( tci <= -64.288 )
								if( ci_wt2 <= -42.6049 )
									ret := 0.780488 // buy
								if( ci_wt2 > -42.6049 )
									ret := 0.572368
							if( tci > -64.288 )
								if( ci <= -119.304 )
									ret := 0.684211
								if( ci > -119.304 )
									ret := -0.114943
						if( ap > 13.1004 )
							if( tci <= -61.1774 )
								if( ap <= 39.6859 )
									ret := 0.138707
								if( ap > 39.6859 )
									ret := 0.409722
							if( tci > -61.1774 )
								if( ap <= 41.0767 )
									ret := 0.249431
								if( ap > 41.0767 )
									ret := 0.698925
				if( ap > 55.2223 )
					if( esa <= 65.7904 )
						if( esa <= 64.3276 )
							if( d_tci <= 59.8302 )
								if( wt2 <= -55.7676 )
									ret := 0.750000 // buy
								if( wt2 > -55.7676 )
									ret := -0.250000
							if( d_tci > 59.8302 )
								if( esa <= 57.7129 )
									ret := -0.187500
								if( esa > 57.7129 )
									ret := -0.636364
						if( esa > 64.3276 )
							ret := -1.000000 // sell
					if( esa > 65.7904 )
						if( tci <= -60.1224 )
							ret := 0.250000
						if( tci > -60.1224 )
							if( esa <= 68.1312 )
								ret := 1.000000 // buy
							if( esa > 68.1312 )
								ret := 0.750000 // buy
			if( d > 0.59572 )
				if( tci <= -70.6001 )
					if( d <= 1.06208 )
						if( esa <= 42.3148 )
							if( esa <= 23.2596 )
								ret := -0.285714
							if( esa > 23.2596 )
								if( d <= 0.683016 )
									ret := 0.307692
								if( d > 0.683016 )
									ret := 0.967742 // buy
						if( esa > 42.3148 )
							if( esa <= 48.0868 )
								if( esa <= 44.1081 )
									ret := -0.500000
								if( esa > 44.1081 )
									ret := -1.000000 // sell
							if( esa > 48.0868 )
								if( ci <= -132.039 )
									ret := -0.800000 // sell
								if( ci > -132.039 )
									ret := 0.657895
					if( d > 1.06208 )
						if( d <= 1.8956 )
							if( d <= 1.41648 )
								if( d <= 1.2224 )
									ret := -1.000000 // sell
								if( d > 1.2224 )
									ret := -0.750000 // sell
							if( d > 1.41648 )
								if( d_tci <= 88.5607 )
									ret := 0.428571
								if( d_tci > 88.5607 )
									ret := -1.000000 // sell
						if( d > 1.8956 )
							ret := 1.000000 // buy
				if( tci > -70.6001 )
					if( tci <= -57.8422 )
						if( ci <= -91.8603 )
							if( wt2 <= -55.4151 )
								if( ci <= -122.431 )
									ret := -0.750000 // sell
								if( ci > -122.431 )
									ret := 0.277778
							if( wt2 > -55.4151 )
								if( ci_wt2 <= -48.1577 )
									ret := 0.967742 // buy
								if( ci_wt2 > -48.1577 )
									ret := 0.200000
						if( ci > -91.8603 )
							if( ci <= -55.8947 )
								if( ci_wt2 <= 6.45302 )
									ret := 0.918699 // buy
								if( ci_wt2 > 6.45302 )
									ret := -0.200000
							if( ci > -55.8947 )
								ret := -0.250000
					if( tci > -57.8422 )
						if( tci <= -57.6911 )
							ret := 0.000000
						if( tci > -57.6911 )
							ret := -0.500000
		if( ci_wt2 > 9.67812 )
			if( wt2 <= -59.9665 )
				if( d_tci <= 59.9386 )
					if( ci_wt2 <= 18.5536 )
						if( ci <= -47.3147 )
							if( tci <= -59.0262 )
								ret := -1.000000 // sell
							if( tci > -59.0262 )
								ret := 0.000000
						if( ci > -47.3147 )
							if( d <= 0.19553 )
								ret := 0.000000
							if( d > 0.19553 )
								if( tci <= -59.1747 )
									ret := 0.800000 // buy
								if( tci > -59.1747 )
									ret := 1.000000 // buy
					if( ci_wt2 > 18.5536 )
						if( ci_wt2 <= 32.0202 )
							if( ap <= 13.7217 )
								if( ap <= 11.7751 )
									ret := -0.250000
								if( ap > 11.7751 )
									ret := -0.923077 // sell
							if( ap > 13.7217 )
								if( ap <= 16.3 )
									ret := 0.250000
								if( ap > 16.3 )
									ret := -0.478261
						if( ci_wt2 > 32.0202 )
							if( ci_wt2 <= 41.1781 )
								if( d <= 0.297594 )
									ret := 0.205128
								if( d > 0.297594 )
									ret := 0.900000 // buy
							if( ci_wt2 > 41.1781 )
								if( wt2 <= -65.2086 )
									ret := 0.137255
								if( wt2 > -65.2086 )
									ret := -0.500000
				if( d_tci > 59.9386 )
					if( ci_wt2 <= 14.0975 )
						if( wt2 <= -61.9723 )
							if( esa <= 22.8991 )
								if( tci <= -67.4643 )
									ret := -0.190476
								if( tci > -67.4643 )
									ret := 0.255814
							if( esa > 22.8991 )
								if( ap <= 24.1667 )
									ret := -1.000000 // sell
								if( ap > 24.1667 )
									ret := -0.278481
						if( wt2 > -61.9723 )
							if( d_tci <= 60.3514 )
								ret := -0.200000
							if( d_tci > 60.3514 )
								if( ci_wt2 <= 13.2778 )
									ret := 0.458333
								if( ci_wt2 > 13.2778 )
									ret := 1.000000 // buy
					if( ci_wt2 > 14.0975 )
						if( d <= 0.732815 )
							if( d <= 0.12862 )
								if( ci <= 18.2085 )
									ret := -0.066298
								if( ci > 18.2085 )
									ret := 0.714286 // buy
							if( d > 0.12862 )
								if( ci <= -58.3106 )
									ret := 0.626506
								if( ci > -58.3106 )
									ret := 0.112060
						if( d > 0.732815 )
							if( esa <= 44.2069 )
								if( wt2 <= -65.6304 )
									ret := 0.906250 // buy
								if( wt2 > -65.6304 )
									ret := -0.250000
							if( esa > 44.2069 )
								if( d_tci <= 76.2362 )
									ret := -0.062500
								if( d_tci > 76.2362 )
									ret := 0.833333 // buy
			if( wt2 > -59.9665 )
				if( ci <= -35.1534 )
					if( esa <= 14.7573 )
						ret := 0.000000
					if( esa > 14.7573 )
						if( esa <= 15.9079 )
							ret := 1.000000 // buy
						if( esa > 15.9079 )
							if( d <= 0.220772 )
								if( d <= 0.122465 )
									ret := 0.615385
								if( d > 0.122465 )
									ret := -0.083333
							if( d > 0.220772 )
								if( ci_wt2 <= 15.4194 )
									ret := 0.947368 // buy
								if( ci_wt2 > 15.4194 )
									ret := 0.400000
				if( ci > -35.1534 )
					if( ci_wt2 <= 30.9488 )
						if( d <= 0.231304 )
							ret := 0.000000
						if( d > 0.231304 )
							if( d_tci <= 58.4486 )
								ret := -1.000000 // sell
							if( d_tci > 58.4486 )
								ret := -0.750000 // sell
					if( ci_wt2 > 30.9488 )
						ret := 0.400000
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_AVAXUSDT_15Min_0e976148(tci, ci, d_tci, esa, d, ci_wt2, wt2, ap)

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


