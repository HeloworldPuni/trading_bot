//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Triple_EMA
// ID_model: SNOW_1Min_2CT0_71070f64 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNOW_1Min_2CT0_71070f64", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNOW_1Min_71070f64(mf, ad, ad_mf, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ad_mf <= -0.674139 )
		if( ad_mf <= -24578.2 )
			if( ad <= -25065.7 )
				if( ema2 <= 154.41 )
					if( mf <= -0.274039 )
						if( ema12 <= -0.302761 )
							if( ema1 <= 123.718 )
								if( ema12 <= -0.345961 )
									ret := 0.735294 // buy
								if( ema12 > -0.345961 )
									ret := -0.111111
							if( ema1 > 123.718 )
								if( ad <= -26512 )
									ret := -0.216667
								if( ad > -26512 )
									ret := 1.000000 // buy
						if( ema12 > -0.302761 )
							if( ema1 <= 120.975 )
								if( ema13 <= -0.228471 )
									ret := 0.557692
								if( ema13 > -0.228471 )
									ret := 0.000000
							if( ema1 > 120.975 )
								if( ad_mf <= -34815.3 )
									ret := 0.649007
								if( ad_mf > -34815.3 )
									ret := 0.288136
					if( mf > -0.274039 )
						if( ad <= -44906.6 )
							if( ad_mf <= -45459.6 )
								if( tema <= 122.672 )
									ret := -0.119048
								if( tema > 122.672 )
									ret := 0.129964
							if( ad_mf > -45459.6 )
								if( ad_mf <= -45006.9 )
									ret := -1.000000 // sell
								if( ad_mf > -45006.9 )
									ret := -0.600000
						if( ad > -44906.6 )
							if( mf <= -0.042249 )
								if( ad_mf <= -26691.1 )
									ret := 0.185714
								if( ad_mf > -26691.1 )
									ret := -0.195402
							if( mf > -0.042249 )
								if( ad <= -25467.4 )
									ret := 0.421053
								if( ad > -25467.4 )
									ret := -0.214286
				if( ema2 > 154.41 )
					if( ema13 <= -1.14985 )
						if( ema13 <= -5.347 )
							ret := 0.250000
						if( ema13 > -5.347 )
							if( ema2 <= 168.895 )
								ret := -1.000000 // sell
							if( ema2 > 168.895 )
								ret := -0.500000
					if( ema13 > -1.14985 )
						if( ema13 <= -0.630523 )
							if( mf <= -0.232674 )
								ret := -0.142857
							if( mf > -0.232674 )
								if( ema3 <= 157.473 )
									ret := 0.500000
								if( ema3 > 157.473 )
									ret := 1.000000 // buy
						if( ema13 > -0.630523 )
							if( mf <= 0.117775 )
								if( ema12 <= -0.000927 )
									ret := -0.219178
								if( ema12 > -0.000927 )
									ret := 0.400000
							if( mf > 0.117775 )
								if( ad <= -51248.6 )
									ret := -0.500000
								if( ad > -51248.6 )
									ret := -1.000000 // sell
			if( ad > -25065.7 )
				if( ema12 <= -0.251305 )
					if( ad_mf <= -24757.6 )
						if( ema13 <= -0.817491 )
							ret := 1.000000 // buy
						if( ema13 > -0.817491 )
							ret := 0.571429
					if( ad_mf > -24757.6 )
						ret := -1.000000 // sell
				if( ema12 > -0.251305 )
					if( tema <= 113.084 )
						ret := 0.333333
					if( tema > 113.084 )
						if( mf <= -0.282373 )
							ret := 0.000000
						if( mf > -0.282373 )
							if( mf <= -0.12781 )
								ret := 1.000000 // buy
							if( mf > -0.12781 )
								if( ad <= -25015.1 )
									ret := 0.500000
								if( ad > -25015.1 )
									ret := 0.906250 // buy
		if( ad_mf > -24578.2 )
			if( ad <= -1474.74 )
				if( ema12 <= 0.04718 )
					if( ad <= -23899.9 )
						if( ad_mf <= -23989.8 )
							if( ema13 <= -0.558727 )
								ret := -1.000000 // sell
							if( ema13 > -0.558727 )
								if( ad_mf <= -24205.3 )
									ret := -0.360000
								if( ad_mf > -24205.3 )
									ret := 0.047619
						if( ad_mf > -23989.8 )
							if( ema12 <= -0.038017 )
								ret := -1.000000 // sell
							if( ema12 > -0.038017 )
								ret := 0.000000
					if( ad > -23899.9 )
						if( tema <= 165.62 )
							if( ad_mf <= -23335.9 )
								if( ema3 <= 146.285 )
									ret := 0.666667
								if( ema3 > 146.285 )
									ret := -0.600000
							if( ad_mf > -23335.9 )
								if( ad_mf <= -2805.44 )
									ret := 0.058189
								if( ad_mf > -2805.44 )
									ret := 0.000793
						if( tema > 165.62 )
							if( tema <= 171.148 )
								if( mf <= -0.41765 )
									ret := -0.500000
								if( mf > -0.41765 )
									ret := 0.579710
							if( tema > 171.148 )
								if( ad_mf <= -7369.07 )
									ret := -1.000000 // sell
								if( ad_mf > -7369.07 )
									ret := 0.125000
				if( ema12 > 0.04718 )
					if( ema2 <= 172.603 )
						if( ad <= -1572.36 )
							if( ema13 <= 0.804512 )
								if( ad <= -1624.26 )
									ret := 0.125553
								if( ad > -1624.26 )
									ret := 0.568966
							if( ema13 > 0.804512 )
								if( mf <= 0.328378 )
									ret := -0.344828
								if( mf > 0.328378 )
									ret := 0.500000
						if( ad > -1572.36 )
							if( ad_mf <= -1565.49 )
								if( ema2 <= 155.65 )
									ret := -0.625000
								if( ema2 > 155.65 )
									ret := -1.000000 // sell
							if( ad_mf > -1565.49 )
								if( ema13 <= 0.094219 )
									ret := -0.583333
								if( ema13 > 0.094219 )
									ret := -0.016393
					if( ema2 > 172.603 )
						ret := -1.000000 // sell
			if( ad > -1474.74 )
				if( ad <= -1454.99 )
					if( ema1 <= 112.82 )
						if( ema1 <= 111.717 )
							ret := 0.200000
						if( ema1 > 111.717 )
							ret := -0.800000 // sell
					if( ema1 > 112.82 )
						if( ema12 <= 0.113405 )
							if( ema2 <= 156.47 )
								if( ema13 <= 0.168714 )
									ret := 0.637681
								if( ema13 > 0.168714 )
									ret := -0.500000
							if( ema2 > 156.47 )
								if( ema13 <= -0.218671 )
									ret := -0.750000 // sell
								if( ema13 > -0.218671 )
									ret := 0.000000
						if( ema12 > 0.113405 )
							ret := 1.000000 // buy
				if( ad > -1454.99 )
					if( mf <= 0.195654 )
						if( ema3 <= 169.974 )
							if( ema12 <= -0.184982 )
								if( mf <= 0.096282 )
									ret := -0.075410
								if( mf > 0.096282 )
									ret := 0.652174
							if( ema12 > -0.184982 )
								if( ad_mf <= -234.202 )
									ret := 0.179243
								if( ad_mf > -234.202 )
									ret := 0.005556
						if( ema3 > 169.974 )
							if( ad <= -694.069 )
								if( ad_mf <= -811.56 )
									ret := -0.375000
								if( ad_mf > -811.56 )
									ret := -0.900000 // sell
							if( ad > -694.069 )
								if( ad_mf <= -250.479 )
									ret := 0.000000
								if( ad_mf > -250.479 )
									ret := 0.750000 // buy
					if( mf > 0.195654 )
						if( ad_mf <= -818.739 )
							if( ema13 <= -0.083761 )
								if( ema3 <= 158.363 )
									ret := -0.687500
								if( ema3 > 158.363 )
									ret := 0.000000
							if( ema13 > -0.083761 )
								if( ema2 <= 162.576 )
									ret := -0.106218
								if( ema2 > 162.576 )
									ret := -0.846154 // sell
						if( ad_mf > -818.739 )
							if( mf <= 0.870271 )
								if( ema12 <= -0.041376 )
									ret := 0.500000
								if( ema12 > -0.041376 )
									ret := 0.077572
							if( mf > 0.870271 )
								if( ad_mf <= -0.883967 )
									ret := -0.037037
								if( ad_mf > -0.883967 )
									ret := 0.965517 // buy
	if( ad_mf > -0.674139 )
		if( ema1 <= 137.159 )
			if( tema <= 109.705 )
				if( ema1 <= 109.012 )
					if( ema2 <= 107.935 )
						if( ema12 <= 0.04079 )
							if( ad_mf <= 0.329216 )
								if( tema <= 107.628 )
									ret := 0.937500 // buy
								if( tema > 107.628 )
									ret := 0.133333
							if( ad_mf > 0.329216 )
								if( ema1 <= 107.407 )
									ret := 0.500000
								if( ema1 > 107.407 )
									ret := -0.074074
						if( ema12 > 0.04079 )
							if( ema13 <= 0.285616 )
								if( ema1 <= 107.777 )
									ret := 0.428571
								if( ema1 > 107.777 )
									ret := 0.909091 // buy
							if( ema13 > 0.285616 )
								ret := 0.250000
					if( ema2 > 107.935 )
						if( ema12 <= 0.009122 )
							if( ad_mf <= 1129.15 )
								if( tema <= 107.702 )
									ret := 1.000000 // buy
								if( tema > 107.702 )
									ret := -0.786885 // sell
							if( ad_mf > 1129.15 )
								if( mf <= -0.021209 )
									ret := -0.307692
								if( mf > -0.021209 )
									ret := 0.080000
						if( ema12 > 0.009122 )
							if( ad_mf <= 8080.48 )
								if( ad <= 92.3452 )
									ret := -0.333333
								if( ad > 92.3452 )
									ret := 0.512821
							if( ad_mf > 8080.48 )
								if( ema2 <= 108.61 )
									ret := 0.000000
								if( ema2 > 108.61 )
									ret := -0.800000 // sell
				if( ema1 > 109.012 )
					if( mf <= -0.208264 )
						if( ema3 <= 108.827 )
							ret := -1.000000 // sell
						if( ema3 > 108.827 )
							if( ad_mf <= 0.270187 )
								if( ema2 <= 109.305 )
									ret := 1.000000 // buy
								if( ema2 > 109.305 )
									ret := 0.600000
							if( ad_mf > 0.270187 )
								if( ad_mf <= 409.157 )
									ret := 0.580645
								if( ad_mf > 409.157 )
									ret := 0.264151
					if( mf > -0.208264 )
						if( ema3 <= 108.922 )
							ret := 1.000000 // buy
						if( ema3 > 108.922 )
							if( ema3 <= 109.45 )
								if( ad_mf <= 0.010587 )
									ret := -0.692308
								if( ad_mf > 0.010587 )
									ret := 0.120301
							if( ema3 > 109.45 )
								if( ad_mf <= 0.05445 )
									ret := 0.804348 // buy
								if( ad_mf > 0.05445 )
									ret := 0.204420
			if( tema > 109.705 )
				if( ema12 <= -0.202698 )
					if( ema1 <= 134.218 )
						if( ad_mf <= 0.411604 )
							if( ema12 <= -0.563005 )
								if( mf <= 0.13324 )
									ret := 0.285714
								if( mf > 0.13324 )
									ret := -1.000000 // sell
							if( ema12 > -0.563005 )
								if( ema3 <= 126.284 )
									ret := 0.537143
								if( ema3 > 126.284 )
									ret := 0.782178 // buy
						if( ad_mf > 0.411604 )
							if( mf <= -0.093497 )
								if( ad <= 17421.8 )
									ret := 0.086580
								if( ad > 17421.8 )
									ret := -0.251799
							if( mf > -0.093497 )
								if( ad_mf <= 38106.4 )
									ret := 0.408088
								if( ad_mf > 38106.4 )
									ret := -0.047619
					if( ema1 > 134.218 )
						if( ad <= 4952.62 )
							if( tema <= 134.237 )
								if( ad_mf <= 0.139176 )
									ret := -0.916667 // sell
								if( ad_mf > 0.139176 )
									ret := 0.333333
							if( tema > 134.237 )
								if( ema2 <= 136.217 )
									ret := -0.973684 // sell
								if( ema2 > 136.217 )
									ret := -0.363636
						if( ad > 4952.62 )
							if( ad_mf <= 10493.5 )
								if( mf <= -0.348908 )
									ret := -0.400000
								if( mf > -0.348908 )
									ret := 0.656250
							if( ad_mf > 10493.5 )
								if( ema13 <= -0.771721 )
									ret := 0.666667
								if( ema13 > -0.771721 )
									ret := -0.482759
				if( ema12 > -0.202698 )
					if( ema13 <= 0.779707 )
						if( mf <= 0.471473 )
							if( ad_mf <= 7258.26 )
								if( ema12 <= 0.015089 )
									ret := 0.059814
								if( ema12 > 0.015089 )
									ret := -0.032102
							if( ad_mf > 7258.26 )
								if( ema13 <= -0.122174 )
									ret := -0.088351
								if( ema13 > -0.122174 )
									ret := 0.112068
						if( mf > 0.471473 )
							if( ema3 <= 127.675 )
								if( ad <= 55036.7 )
									ret := -0.265116
								if( ad > 55036.7 )
									ret := 0.452381
							if( ema3 > 127.675 )
								if( ad_mf <= 51966.4 )
									ret := 0.068627
								if( ad_mf > 51966.4 )
									ret := -0.681818
					if( ema13 > 0.779707 )
						if( ema12 <= 0.893719 )
							if( ema2 <= 111.941 )
								if( mf <= 0.134701 )
									ret := -0.642857
								if( mf > 0.134701 )
									ret := 0.550000
							if( ema2 > 111.941 )
								if( ema2 <= 134.729 )
									ret := -0.520000
								if( ema2 > 134.729 )
									ret := 0.200000
						if( ema12 > 0.893719 )
							if( tema <= 118.938 )
								if( ema1 <= 116.625 )
									ret := 1.000000 // buy
								if( ema1 > 116.625 )
									ret := 0.500000
							if( tema > 118.938 )
								ret := -0.750000 // sell
		if( ema1 > 137.159 )
			if( ema12 <= 0.087503 )
				if( ema2 <= 160.74 )
					if( ad_mf <= 1755.12 )
						if( ema1 <= 159.937 )
							if( ema3 <= 137.275 )
								if( ema12 <= 0.079652 )
									ret := -0.615385
								if( ema12 > 0.079652 )
									ret := 0.200000
							if( ema3 > 137.275 )
								if( mf <= 0.625893 )
									ret := 0.051109
								if( mf > 0.625893 )
									ret := -0.800000 // sell
						if( ema1 > 159.937 )
							if( ema13 <= 0.095694 )
								if( ad <= 147.929 )
									ret := -0.390625
								if( ad > 147.929 )
									ret := 0.012987
							if( ema13 > 0.095694 )
								if( ema3 <= 160.183 )
									ret := -1.000000 // sell
								if( ema3 > 160.183 )
									ret := -0.708333 // sell
					if( ad_mf > 1755.12 )
						if( ema12 <= -0.3258 )
							if( ema12 <= -0.762956 )
								if( ad_mf <= 115521 )
									ret := 0.550000
								if( ad_mf > 115521 )
									ret := -1.000000 // sell
							if( ema12 > -0.762956 )
								if( mf <= -0.090277 )
									ret := -0.146341
								if( mf > -0.090277 )
									ret := -0.640000
						if( ema12 > -0.3258 )
							if( ad <= 3579.26 )
								if( ema13 <= -0.499434 )
									ret := 0.666667
								if( ema13 > -0.499434 )
									ret := -0.141645
							if( ad > 3579.26 )
								if( ad_mf <= 4017.67 )
									ret := 0.161572
								if( ad_mf > 4017.67 )
									ret := -0.024697
				if( ema2 > 160.74 )
					if( ema2 <= 163.561 )
						if( ema12 <= -0.074559 )
							if( ad <= 449.5 )
								if( ema13 <= -0.50153 )
									ret := 0.000000
								if( ema13 > -0.50153 )
									ret := 0.857143 // buy
							if( ad > 449.5 )
								if( mf <= -0.355266 )
									ret := 0.846154 // buy
								if( mf > -0.355266 )
									ret := 0.083969
						if( ema12 > -0.074559 )
							if( ema12 <= 0.023353 )
								if( ema12 <= -0.013865 )
									ret := 0.095238
								if( ema12 > -0.013865 )
									ret := 0.298643
							if( ema12 > 0.023353 )
								if( ad <= 149.925 )
									ret := -0.244444
								if( ad > 149.925 )
									ret := 0.097345
					if( ema2 > 163.561 )
						if( tema <= 163.675 )
							if( ema1 <= 163.487 )
								if( tema <= 162.895 )
									ret := -1.000000 // sell
								if( tema > 162.895 )
									ret := -0.750000 // sell
							if( ema1 > 163.487 )
								if( ema1 <= 163.69 )
									ret := -0.043478
								if( ema1 > 163.69 )
									ret := -0.750000 // sell
						if( tema > 163.675 )
							if( tema <= 163.985 )
								if( ema1 <= 163.992 )
									ret := 0.148649
								if( ema1 > 163.992 )
									ret := 0.851852 // buy
							if( tema > 163.985 )
								if( ema13 <= -0.67919 )
									ret := 0.619048
								if( ema13 > -0.67919 )
									ret := -0.089869
			if( ema12 > 0.087503 )
				if( ad <= 905 )
					if( ema13 <= 0.959084 )
						if( ema3 <= 137.082 )
							if( ema2 <= 137.075 )
								ret := -0.500000
							if( ema2 > 137.075 )
								if( mf <= 0.405875 )
									ret := -1.000000 // sell
								if( mf > 0.405875 )
									ret := -0.600000
						if( ema3 > 137.082 )
							if( ema3 <= 137.887 )
								if( ad_mf <= -0.136424 )
									ret := 0.730769 // buy
								if( ad_mf > -0.136424 )
									ret := -0.270270
							if( ema3 > 137.887 )
								if( ema12 <= 0.168521 )
									ret := -0.254083
								if( ema12 > 0.168521 )
									ret := -0.413437
					if( ema13 > 0.959084 )
						if( ema2 <= 154.903 )
							ret := -1.000000 // sell
						if( ema2 > 154.903 )
							if( ema12 <= 0.778697 )
								if( ema13 <= 1.36296 )
									ret := 1.000000 // buy
								if( ema13 > 1.36296 )
									ret := 0.714286 // buy
							if( ema12 > 0.778697 )
								ret := 0.250000
				if( ad > 905 )
					if( ema13 <= 0.865247 )
						if( ad <= 1348.71 )
							if( ad_mf <= 1310.93 )
								if( ad <= 993.2 )
									ret := 0.521739
								if( ad > 993.2 )
									ret := -0.010638
							if( ad_mf > 1310.93 )
								if( ema12 <= 0.294713 )
									ret := 0.944444 // buy
								if( ema12 > 0.294713 )
									ret := 0.400000
						if( ad > 1348.71 )
							if( ad <= 1552.41 )
								if( mf <= -0.145992 )
									ret := -1.000000 // sell
								if( mf > -0.145992 )
									ret := -0.380952
							if( ad > 1552.41 )
								if( ad <= 1762.01 )
									ret := 0.442308
								if( ad > 1762.01 )
									ret := -0.046791
					if( ema13 > 0.865247 )
						if( ema2 <= 157.579 )
							if( ad <= 14710.8 )
								if( ad <= 9321.42 )
									ret := -0.538462
								if( ad > 9321.42 )
									ret := 0.750000 // buy
							if( ad > 14710.8 )
								if( mf <= 0.503821 )
									ret := -0.937500 // sell
								if( mf > 0.503821 )
									ret := -0.250000
						if( ema2 > 157.579 )
							if( mf <= 0.303569 )
								ret := -1.000000 // sell
							if( mf > 0.303569 )
								ret := -0.750000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Chaikin_Money_Flow 
 //@version=5
//indicator title="Chaikin Money Flow", shorttitle="CMF", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
var cumVol = 0.
cumVol += nz(volume)
if barstate.islast and cumVol == 0
    runtime.error("No volume is provided by the data vendor.")
length_CMF = input.int(20, minval=1)
ad = close==high and close==low or high==low ? 0 : ((2*close-low-high)/(high-low))*volume
mf = math.sum(ad, length_CMF) / math.sum(volume, length_CMF)
plot(mf, color=#43A047, title="MF")
hline(0, color=#787B86, title="Zero", linestyle=hline.style_dashed)


ad_mf = ad - mf

//CODE associated with the technical indicator L_Triple_EMA 
//@version=5
//indicator title="Triple EMA", shorttitle="TEMA", overlay=true, timeframe="", timeframe_gaps=true)
length_TEMA = input.int(9, minval=1)
ema1 = ta.ema(close, length_TEMA)
ema2 = ta.ema(ema1, length_TEMA)
ema3 = ta.ema(ema2, length_TEMA)
tema = 3 * (ema1 - ema2) + ema3
plot(tema, "TEMA", color=#2962FF)

ema12 = ema1 - ema2
ema13 = ema1 - ema3


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
float op_operation = decision_tree_0_SNOW_1Min_71070f64(mf, ad, ad_mf, ema1, tema, ema12, ema2, ema3, ema13)

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


