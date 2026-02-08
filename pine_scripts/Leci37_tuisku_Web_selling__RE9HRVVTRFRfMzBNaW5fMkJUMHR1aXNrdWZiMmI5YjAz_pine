//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Triple_EMA
// ID_model: DOGEUSDT_30Min_2BT0_fb2b9b03 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOGEUSDT_30Min_2BT0_fb2b9b03", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOGEUSDT_30Min_fb2b9b03(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( bullPower <= -0.001402 )
		if( ema1 <= 0.247578 )
			if( bearPower <= -0.006668 )
				if( ema3 <= 0.257758 )
					if( ema3 <= 0.128872 )
						if( tema <= 0.117532 )
							if( ema12 <= -0.00247 )
								if( ema13 <= -0.00719 )
									ret := -0.200000
								if( ema13 > -0.00719 )
									ret := 0.698925
							if( ema12 > -0.00247 )
								if( bullPower <= -0.001929 )
									ret := -0.565217
								if( bullPower > -0.001929 )
									ret := 1.000000 // buy
						if( tema > 0.117532 )
							if( ema3 <= 0.127859 )
								ret := -0.500000
							if( ema3 > 0.127859 )
								ret := -1.000000 // sell
					if( ema3 > 0.128872 )
						if( ema1 <= 0.239159 )
							if( ema3 <= 0.150351 )
								if( ema1 <= 0.135792 )
									ret := 1.000000 // buy
								if( ema1 > 0.135792 )
									ret := 0.777778 // buy
							if( ema3 > 0.150351 )
								if( bearPower <= -0.017514 )
									ret := 0.862069 // buy
								if( bearPower > -0.017514 )
									ret := 0.457317
						if( ema1 > 0.239159 )
							if( ema13 <= -0.003716 )
								if( ema13 <= -0.008839 )
									ret := 0.833333 // buy
								if( ema13 > -0.008839 )
									ret := 1.000000 // buy
							if( ema13 > -0.003716 )
								if( tema <= 0.239785 )
									ret := 1.000000 // buy
								if( tema > 0.239785 )
									ret := 0.250000
				if( ema3 > 0.257758 )
					if( ema3 <= 0.260594 )
						ret := -1.000000 // sell
					if( ema3 > 0.260594 )
						ret := -0.750000 // sell
			if( bearPower > -0.006668 )
				if( ema13 <= -0.00455 )
					if( tema <= 0.128087 )
						if( bearPower <= -0.003937 )
							if( bearPower <= -0.006212 )
								if( ema2 <= 0.113441 )
									ret := -0.769231 // sell
								if( ema2 > 0.113441 )
									ret := 1.000000 // buy
							if( bearPower > -0.006212 )
								if( ema12 <= -0.003544 )
									ret := 0.076923
								if( ema12 > -0.003544 )
									ret := 0.888889 // buy
						if( bearPower > -0.003937 )
							if( ema12 <= -0.002584 )
								if( tema <= 0.100054 )
									ret := 0.250000
								if( tema > 0.100054 )
									ret := -0.250000
							if( ema12 > -0.002584 )
								if( bearPower <= -0.003369 )
									ret := -0.888889 // sell
								if( bearPower > -0.003369 )
									ret := -0.250000
					if( tema > 0.128087 )
						if( bearPower <= -0.005791 )
							if( bbm <= 0.002585 )
								if( ema13 <= -0.007441 )
									ret := -1.000000 // sell
								if( ema13 > -0.007441 )
									ret := -0.200000
							if( bbm > 0.002585 )
								if( bbm <= 0.004457 )
									ret := 0.536585
								if( bbm > 0.004457 )
									ret := -0.500000
						if( bearPower > -0.005791 )
							if( tema <= 0.131905 )
								if( bbm <= 0.002788 )
									ret := -1.000000 // sell
								if( bbm > 0.002788 )
									ret := -0.250000
							if( tema > 0.131905 )
								if( tema <= 0.151889 )
									ret := 0.200000
								if( tema > 0.151889 )
									ret := -0.428571
				if( ema13 > -0.00455 )
					if( tema <= 0.198375 )
						if( ema3 <= 0.197113 )
							if( ema12 <= -0.001502 )
								if( ema1 <= 0.083093 )
									ret := 0.633094
								if( ema1 > 0.083093 )
									ret := 0.274725
							if( ema12 > -0.001502 )
								if( bbp <= -0.006001 )
									ret := 0.470588
								if( bbp > -0.006001 )
									ret := 0.056566
						if( ema3 > 0.197113 )
							if( ema1 <= 0.196162 )
								if( bullPower <= -0.001934 )
									ret := -0.500000
								if( bullPower > -0.001934 )
									ret := -1.000000 // sell
							if( ema1 > 0.196162 )
								if( bbm <= 0.003181 )
									ret := 0.000000
								if( bbm > 0.003181 )
									ret := -0.750000 // sell
					if( tema > 0.198375 )
						if( ema13 <= -0.001446 )
							if( bbm <= 0.002209 )
								if( bullPower <= -0.001602 )
									ret := 0.525000
								if( bullPower > -0.001602 )
									ret := -0.041667
							if( bbm > 0.002209 )
								if( ema13 <= -0.003571 )
									ret := 0.516129
								if( ema13 > -0.003571 )
									ret := 0.790323 // buy
						if( ema13 > -0.001446 )
							if( bullPower <= -0.00153 )
								if( bbp <= -0.005899 )
									ret := 0.416667
								if( bbp > -0.005899 )
									ret := 0.000000
							if( bullPower > -0.00153 )
								if( bbp <= -0.004803 )
									ret := -0.875000 // sell
								if( bbp > -0.004803 )
									ret := -0.250000
		if( ema1 > 0.247578 )
			if( bullPower <= -0.006351 )
				if( ema13 <= -0.052523 )
					if( ema2 <= 0.531954 )
						ret := 0.800000 // buy
					if( ema2 > 0.531954 )
						ret := -1.000000 // sell
				if( ema13 > -0.052523 )
					if( ema12 <= -0.013948 )
						if( bbm <= 0.015155 )
							ret := 0.500000
						if( bbm > 0.015155 )
							if( bullPower <= -0.011557 )
								if( bbm <= 0.028393 )
									ret := 0.937500 // buy
								if( bbm > 0.028393 )
									ret := 1.000000 // buy
							if( bullPower > -0.011557 )
								if( bbp <= -0.057655 )
									ret := 0.142857
								if( bbp > -0.057655 )
									ret := 1.000000 // buy
					if( ema12 > -0.013948 )
						if( ema13 <= -0.010927 )
							if( ema3 <= 0.313226 )
								if( bullPower <= -0.006787 )
									ret := 0.973684 // buy
								if( bullPower > -0.006787 )
									ret := 0.666667
							if( ema3 > 0.313226 )
								if( ema1 <= 0.313361 )
									ret := -1.000000 // sell
								if( ema1 > 0.313361 )
									ret := 0.323077
						if( ema13 > -0.010927 )
							if( ema1 <= 0.586041 )
								if( ema2 <= 0.259023 )
									ret := -1.000000 // sell
								if( ema2 > 0.259023 )
									ret := 0.147541
							if( ema1 > 0.586041 )
								ret := -1.000000 // sell
			if( bullPower > -0.006351 )
				if( tema <= 0.269503 )
					if( bullPower <= -0.001591 )
						if( ema1 <= 0.255391 )
							if( bullPower <= -0.003489 )
								if( bullPower <= -0.004741 )
									ret := 0.200000
								if( bullPower > -0.004741 )
									ret := 0.850000 // buy
							if( bullPower > -0.003489 )
								if( ema13 <= -0.004072 )
									ret := 0.058824
								if( ema13 > -0.004072 )
									ret := -0.678571
						if( ema1 > 0.255391 )
							if( ema13 <= -0.011843 )
								if( bbm <= 0.012554 )
									ret := -0.571429
								if( bbm > 0.012554 )
									ret := -1.000000 // sell
							if( ema13 > -0.011843 )
								if( ema12 <= -0.004544 )
									ret := 0.044444
								if( ema12 > -0.004544 )
									ret := -0.467391
					if( bullPower > -0.001591 )
						if( ema2 <= 0.255389 )
							ret := -0.400000
						if( ema2 > 0.255389 )
							if( ema12 <= -0.003323 )
								ret := 1.000000 // buy
							if( ema12 > -0.003323 )
								if( ema1 <= 0.263327 )
									ret := 0.800000 // buy
								if( ema1 > 0.263327 )
									ret := 0.000000
				if( tema > 0.269503 )
					if( ema1 <= 0.302159 )
						if( ema1 <= 0.291195 )
							if( ema13 <= -0.009216 )
								if( ema13 <= -0.010952 )
									ret := -0.500000
								if( ema13 > -0.010952 )
									ret := -1.000000 // sell
							if( ema13 > -0.009216 )
								if( ema3 <= 0.295282 )
									ret := 0.495413
								if( ema3 > 0.295282 )
									ret := -0.600000
						if( ema1 > 0.291195 )
							if( ema3 <= 0.306404 )
								if( ema2 <= 0.300519 )
									ret := 0.959459 // buy
								if( ema2 > 0.300519 )
									ret := 0.588235
							if( ema3 > 0.306404 )
								if( ema12 <= -0.005951 )
									ret := 0.200000
								if( ema12 > -0.005951 )
									ret := -0.800000 // sell
					if( ema1 > 0.302159 )
						if( tema <= 0.302833 )
							if( ema3 <= 0.305423 )
								ret := 1.000000 // buy
							if( ema3 > 0.305423 )
								if( tema <= 0.295075 )
									ret := 0.500000
								if( tema > 0.295075 )
									ret := -0.956522 // sell
						if( tema > 0.302833 )
							if( ema3 <= 0.325862 )
								if( ema2 <= 0.322283 )
									ret := 0.236842
								if( ema2 > 0.322283 )
									ret := 0.933333 // buy
							if( ema3 > 0.325862 )
								if( ema13 <= -0.000536 )
									ret := 0.002315
								if( ema13 > -0.000536 )
									ret := 0.857143 // buy
	if( bullPower > -0.001402 )
		if( bbp <= 0.00447 )
			if( tema <= 0.067685 )
				if( bbm <= 0.0005 )
					if( tema <= 0.008654 )
						if( bbp <= -0.000364 )
							if( ema1 <= 0.008347 )
								if( ema1 <= 0.003864 )
									ret := 0.571429
								if( ema1 > 0.003864 )
									ret := 0.963636 // buy
							if( ema1 > 0.008347 )
								if( tema <= 0.008194 )
									ret := -0.500000
								if( tema > 0.008194 )
									ret := 0.666667
						if( bbp > -0.000364 )
							if( bearPower <= -2e-05 )
								if( ema13 <= -0.000105 )
									ret := -0.153488
								if( ema13 > -0.000105 )
									ret := 0.238350
							if( bearPower > -2e-05 )
								if( ema3 <= 0.004923 )
									ret := 0.015581
								if( ema3 > 0.004923 )
									ret := 0.387387
					if( tema > 0.008654 )
						if( ema2 <= 0.009033 )
							if( tema <= 0.009023 )
								if( bearPower <= -0.000103 )
									ret := 0.333333
								if( bearPower > -0.000103 )
									ret := -0.401198
							if( tema > 0.009023 )
								if( bullPower <= 7.9e-05 )
									ret := -0.500000
								if( bullPower > 7.9e-05 )
									ret := -1.000000 // sell
						if( ema2 > 0.009033 )
							if( ema1 <= 0.009356 )
								if( ema12 <= -0.000226 )
									ret := -0.923077 // sell
								if( ema12 > -0.000226 )
									ret := 0.361516
							if( ema1 > 0.009356 )
								if( ema3 <= 0.009384 )
									ret := -0.750000 // sell
								if( ema3 > 0.009384 )
									ret := 0.043942
				if( bbm > 0.0005 )
					if( tema <= 0.050741 )
						if( tema <= 0.048042 )
							if( tema <= 0.045916 )
								if( ema1 <= 0.038217 )
									ret := 0.152878
								if( ema1 > 0.038217 )
									ret := 0.455056
							if( tema > 0.045916 )
								if( bbp <= 0.000437 )
									ret := -0.518987
								if( bbp > 0.000437 )
									ret := 0.395349
						if( tema > 0.048042 )
							if( ema3 <= 0.052541 )
								if( ema1 <= 0.050921 )
									ret := 0.458763
								if( ema1 > 0.050921 )
									ret := -0.655172
							if( ema3 > 0.052541 )
								if( bbp <= -0.001658 )
									ret := 0.976190 // buy
								if( bbp > -0.001658 )
									ret := 0.750000 // buy
					if( tema > 0.050741 )
						if( tema <= 0.052957 )
							if( ema12 <= -0.000957 )
								if( tema <= 0.052336 )
									ret := 0.809524 // buy
								if( tema > 0.052336 )
									ret := 0.000000
							if( ema12 > -0.000957 )
								if( bearPower <= -0.001046 )
									ret := -0.657407
								if( bearPower > -0.001046 )
									ret := -0.055351
						if( tema > 0.052957 )
							if( ema2 <= 0.066341 )
								if( tema <= 0.055533 )
									ret := 0.268477
								if( tema > 0.055533 )
									ret := 0.091674
							if( ema2 > 0.066341 )
								if( ema1 <= 0.066853 )
									ret := 0.486322
								if( ema1 > 0.066853 )
									ret := 0.156069
			if( tema > 0.067685 )
				if( ema13 <= 0.003446 )
					if( ema1 <= 0.515917 )
						if( bbm <= 0.002103 )
							if( tema <= 0.169665 )
								if( ema12 <= -0.000414 )
									ret := 0.087271
								if( ema12 > -0.000414 )
									ret := 0.009892
							if( tema > 0.169665 )
								if( ema2 <= 0.182021 )
									ret := -0.141213
								if( ema2 > 0.182021 )
									ret := -0.017045
						if( bbm > 0.002103 )
							if( ema2 <= 0.313319 )
								if( bbp <= -0.000916 )
									ret := 0.176548
								if( bbp > -0.000916 )
									ret := 0.034152
							if( ema2 > 0.313319 )
								if( ema3 <= 0.315533 )
									ret := -0.711538 // sell
								if( ema3 > 0.315533 )
									ret := -0.060676
					if( ema1 > 0.515917 )
						if( ema12 <= -0.006766 )
							if( ema3 <= 0.549888 )
								if( ema2 <= 0.531432 )
									ret := 0.500000
								if( ema2 > 0.531432 )
									ret := 1.000000 // buy
							if( ema3 > 0.549888 )
								if( ema1 <= 0.624179 )
									ret := -0.333333
								if( ema1 > 0.624179 )
									ret := -0.875000 // sell
						if( ema12 > -0.006766 )
							if( ema2 <= 0.546925 )
								if( ema13 <= -0.011361 )
									ret := -0.875000 // sell
								if( ema13 > -0.011361 )
									ret := -1.000000 // sell
							if( ema2 > 0.546925 )
								if( tema <= 0.550539 )
									ret := 0.400000
								if( tema > 0.550539 )
									ret := -0.700000 // sell
				if( ema13 > 0.003446 )
					if( bbm <= 0.007654 )
						if( bbm <= 0.006551 )
							if( ema2 <= 0.28093 )
								if( ema3 <= 0.223789 )
									ret := 0.269481
								if( ema3 > 0.223789 )
									ret := -0.261364
							if( ema2 > 0.28093 )
								if( ema12 <= 0.001371 )
									ret := -0.230769
								if( ema12 > 0.001371 )
									ret := 0.594059
						if( bbm > 0.006551 )
							if( ema13 <= 0.007715 )
								if( ema3 <= 0.193993 )
									ret := 0.375000
								if( ema3 > 0.193993 )
									ret := -0.617647
							if( ema13 > 0.007715 )
								ret := 1.000000 // buy
					if( bbm > 0.007654 )
						if( ema2 <= 0.553886 )
							if( ema12 <= 0.003616 )
								if( tema <= 0.235816 )
									ret := 0.230769
								if( tema > 0.235816 )
									ret := 0.790698 // buy
							if( ema12 > 0.003616 )
								if( bullPower <= 0.006024 )
									ret := -0.857143 // sell
								if( bullPower > 0.006024 )
									ret := 0.409091
						if( ema2 > 0.553886 )
							if( bullPower <= 0.008469 )
								if( ema1 <= 0.611297 )
									ret := 0.000000
								if( ema1 > 0.611297 )
									ret := -1.000000 // sell
							if( bullPower > 0.008469 )
								if( ema3 <= 0.62784 )
									ret := 0.000000
								if( ema3 > 0.62784 )
									ret := 1.000000 // buy
		if( bbp > 0.00447 )
			if( ema2 <= 0.032503 )
				if( ema1 <= 0.015755 )
					ret := -1.000000 // sell
				if( ema1 > 0.015755 )
					if( ema12 <= 0.001916 )
						ret := 0.000000
					if( ema12 > 0.001916 )
						if( ema12 <= 0.002609 )
							ret := 1.000000 // buy
						if( ema12 > 0.002609 )
							if( tema <= 0.038318 )
								ret := -0.500000
							if( tema > 0.038318 )
								ret := 1.000000 // buy
			if( ema2 > 0.032503 )
				if( ema2 <= 0.301828 )
					if( tema <= 0.19298 )
						if( ema13 <= 0.006329 )
							if( ema1 <= 0.152235 )
								if( ema13 <= 0.00192 )
									ret := -0.008065
								if( ema13 > 0.00192 )
									ret := -0.239044
							if( ema1 > 0.152235 )
								if( tema <= 0.15954 )
									ret := 0.500000
								if( tema > 0.15954 )
									ret := -0.032630
						if( ema13 > 0.006329 )
							if( ema2 <= 0.088715 )
								if( bearPower <= 0.002672 )
									ret := 0.153846
								if( bearPower > 0.002672 )
									ret := -0.950000 // sell
							if( ema2 > 0.088715 )
								if( bbm <= 0.00589 )
									ret := 0.661376
								if( bbm > 0.00589 )
									ret := -0.030864
					if( tema > 0.19298 )
						if( ema2 <= 0.193062 )
							if( ema13 <= 0.026723 )
								if( ema13 <= 0.007607 )
									ret := -0.696429
								if( ema13 > 0.007607 )
									ret := -0.955224 // sell
							if( ema13 > 0.026723 )
								if( ema3 <= 0.167862 )
									ret := 1.000000 // buy
								if( ema3 > 0.167862 )
									ret := -1.000000 // sell
						if( ema2 > 0.193062 )
							if( ema2 <= 0.244753 )
								if( ema2 <= 0.237461 )
									ret := -0.198185
								if( ema2 > 0.237461 )
									ret := 0.432584
							if( ema2 > 0.244753 )
								if( ema1 <= 0.257175 )
									ret := -0.574297
								if( ema1 > 0.257175 )
									ret := -0.188192
				if( ema2 > 0.301828 )
					if( ema12 <= -0.002603 )
						if( bearPower <= -0.001805 )
							if( ema13 <= -0.019326 )
								ret := -0.500000
							if( ema13 > -0.019326 )
								ret := -1.000000 // sell
						if( bearPower > -0.001805 )
							ret := -0.250000
					if( ema12 > -0.002603 )
						if( tema <= 0.715112 )
							if( ema2 <= 0.660084 )
								if( bearPower <= -0.002314 )
									ret := 0.424460
								if( bearPower > -0.002314 )
									ret := -0.027778
							if( ema2 > 0.660084 )
								if( ema3 <= 0.699351 )
									ret := 1.000000 // buy
								if( ema3 > 0.699351 )
									ret := 0.750000 // buy
						if( tema > 0.715112 )
							ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0


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
float op_operation = decision_tree_0_DOGEUSDT_30Min_fb2b9b03(bearPower, bbm, bbp, bullPower, BBPower_Color, ema12, ema3, ema13, tema, ema1, ema2)

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


