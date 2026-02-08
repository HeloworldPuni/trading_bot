//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Madrid_Moving_Average_Ribbon
// ID_model: APPS_15Min_1MAD_43d49d1f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_APPS_15Min_1MAD_43d49d1f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_APPS_15Min_43d49d1f(ma65, ma15_colorInt, ma90_colorInt, ma75, ma10_colorInt, ma100, ma65_colorInt, ma50, ma55_colorInt, ma80_colorInt, ma70, ma20, ma30_colorInt, ma60, ma05, ma25, ma60_colorInt, ma35, ma25_colorInt, ma05_colorInt, ma90, ma80, ma40_colorInt, ma85, ma75_colorInt, ma30, ma40, ma55, ma15, ma35_colorInt, ma70_colorInt, ma45, ma20_colorInt, ma10, ma45_colorInt, ma85_colorInt, ma50_colorInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( ma15_colorInt <= 3.5 )
		if( ma05_colorInt <= 1.5 )
			if( ma15 <= 1.26501 )
				if( ma100 <= 1.17376 )
					if( ma15 <= 0.675209 )
						if( ma60 <= 0.626953 )
							ret := -0.200000
						if( ma60 > 0.626953 )
							if( ma90 <= 0.632306 )
								ret := 1.000000 // buy
							if( ma90 > 0.632306 )
								ret := 0.500000
					if( ma15 > 0.675209 )
						if( ma25 <= 0.684 )
							if( ma30_colorInt <= 2 )
								if( ma35 <= 0.671658 )
									ret := -1.000000 // sell
								if( ma35 > 0.671658 )
									ret := -0.111111
							if( ma30_colorInt > 2 )
								if( ma05 <= 0.684126 )
									ret := -0.750000 // sell
								if( ma05 > 0.684126 )
									ret := -1.000000 // sell
						if( ma25 > 0.684 )
							if( ma15 <= 0.689929 )
								if( ma80 <= 0.685833 )
									ret := 0.842105 // buy
								if( ma80 > 0.685833 )
									ret := -0.250000
							if( ma15 > 0.689929 )
								if( ma55 <= 0.691527 )
									ret := -0.612245
								if( ma55 > 0.691527 )
									ret := -0.159172
				if( ma100 > 1.17376 )
					if( ma65_colorInt <= 1.5 )
						if( ma35 <= 1.1963 )
							if( ma40 <= 1.18676 )
								if( ma40 <= 1.17974 )
									ret := -0.250000
								if( ma40 > 1.17974 )
									ret := -0.928571 // sell
							if( ma40 > 1.18676 )
								if( ma75 <= 1.18966 )
									ret := -0.076923
								if( ma75 > 1.18966 )
									ret := -0.500000
						if( ma35 > 1.1963 )
							if( ma10 <= 1.22881 )
								if( ma10 <= 1.19639 )
									ret := -0.500000
								if( ma10 > 1.19639 )
									ret := -0.962264 // sell
							if( ma10 > 1.22881 )
								if( ma35 <= 1.21805 )
									ret := 0.000000
								if( ma35 > 1.21805 )
									ret := -0.678571
					if( ma65_colorInt > 1.5 )
						if( ma20_colorInt <= 1.5 )
							if( ma15 <= 1.23397 )
								if( ma45_colorInt <= 2.5 )
									ret := -0.500000
								if( ma45_colorInt > 2.5 )
									ret := 0.521739
							if( ma15 > 1.23397 )
								if( ma35 <= 1.25043 )
									ret := -0.411765
								if( ma35 > 1.25043 )
									ret := 0.500000
						if( ma20_colorInt > 1.5 )
							if( ma25 <= 1.2168 )
								if( ma10 <= 1.20221 )
									ret := -1.000000 // sell
								if( ma10 > 1.20221 )
									ret := -0.750000 // sell
							if( ma25 > 1.2168 )
								if( ma50 <= 1.24077 )
									ret := 0.142857
								if( ma50 > 1.24077 )
									ret := -1.000000 // sell
			if( ma15 > 1.26501 )
				if( ma80 <= 86.878 )
					if( ma15 <= 27.5421 )
						if( ma40 <= 25.9351 )
							if( ma50 <= 1.2477 )
								if( ma25 <= 1.26112 )
									ret := 0.600000
								if( ma25 > 1.26112 )
									ret := 1.000000 // buy
							if( ma50 > 1.2477 )
								if( ma20_colorInt <= 1.5 )
									ret := -0.039364
								if( ma20_colorInt > 1.5 )
									ret := 0.074048
						if( ma40 > 25.9351 )
							if( ma40 <= 26.7185 )
								if( ma50 <= 26.4707 )
									ret := -0.558559
								if( ma50 > 26.4707 )
									ret := 0.200000
							if( ma40 > 26.7185 )
								if( ma55_colorInt <= 1.5 )
									ret := -0.758065 // sell
								if( ma55_colorInt > 1.5 )
									ret := -0.285714
					if( ma15 > 27.5421 )
						if( ma65 <= 30.8513 )
							if( ma50 <= 28.4742 )
								if( ma30 <= 28.224 )
									ret := 0.483516
								if( ma30 > 28.224 )
									ret := -0.724138 // sell
							if( ma50 > 28.4742 )
								if( ma05 <= 32.5978 )
									ret := 0.773196 // buy
								if( ma05 > 32.5978 )
									ret := -0.200000
						if( ma65 > 30.8513 )
							if( ma100 <= 30.3409 )
								ret := -1.000000 // sell
							if( ma100 > 30.3409 )
								if( ma80 <= 30.9564 )
									ret := 0.666667
								if( ma80 > 30.9564 )
									ret := 0.037386
				if( ma80 > 86.878 )
					if( ma05 <= 94.9942 )
						if( ma15 <= 93.9958 )
							if( ma100 <= 90.8125 )
								if( ma05 <= 90.1494 )
									ret := -0.541985
								if( ma05 > 90.1494 )
									ret := -0.200000
							if( ma100 > 90.8125 )
								if( ma05 <= 93.0552 )
									ret := -1.000000 // sell
								if( ma05 > 93.0552 )
									ret := -0.750000 // sell
						if( ma15 > 93.9958 )
							if( ma65 <= 92.9285 )
								if( ma25 <= 93.7809 )
									ret := 0.000000
								if( ma25 > 93.7809 )
									ret := 0.900000 // buy
							if( ma65 > 92.9285 )
								ret := -0.166667
					if( ma05 > 94.9942 )
						if( ma100 <= 92.4246 )
							if( ma20 <= 95.1727 )
								ret := -1.000000 // sell
							if( ma20 > 95.1727 )
								ret := -0.833333 // sell
						if( ma100 > 92.4246 )
							ret := -0.666667
		if( ma05_colorInt > 1.5 )
			if( ma100 <= 5.76279 )
				if( ma05_colorInt <= 3.5 )
					if( ma05 <= 1.15077 )
						if( ma05_colorInt <= 2.5 )
							if( ma70 <= 0.685085 )
								if( ma45_colorInt <= 3.5 )
									ret := 0.886792 // buy
								if( ma45_colorInt > 3.5 )
									ret := 0.142857
							if( ma70 > 0.685085 )
								if( ma55 <= 0.696009 )
									ret := -0.117647
								if( ma55 > 0.696009 )
									ret := 0.221992
						if( ma05_colorInt > 2.5 )
							if( ma50_colorInt <= 2.5 )
								if( ma15_colorInt <= 2.5 )
									ret := 0.737069 // buy
								if( ma15_colorInt > 2.5 )
									ret := 0.547009
							if( ma50_colorInt > 2.5 )
								if( ma50 <= 0.924809 )
									ret := 0.176471
								if( ma50 > 0.924809 )
									ret := 0.481625
					if( ma05 > 1.15077 )
						if( ma55 <= 5.44698 )
							if( ma75 <= 5.11695 )
								if( ma45 <= 2.64168 )
									ret := 0.151390
								if( ma45 > 2.64168 )
									ret := 0.224658
							if( ma75 > 5.11695 )
								if( ma15 <= 5.02063 )
									ret := -0.561644
								if( ma15 > 5.02063 )
									ret := 0.026646
						if( ma55 > 5.44698 )
							if( ma05 <= 5.31783 )
								if( ma85 <= 5.63453 )
									ret := 1.000000 // buy
								if( ma85 > 5.63453 )
									ret := 0.500000
							if( ma05 > 5.31783 )
								if( ma55 <= 5.54022 )
									ret := 0.459184
								if( ma55 > 5.54022 )
									ret := 0.205433
				if( ma05_colorInt > 3.5 )
					if( ma15 <= 4.33272 )
						if( ma05 <= 0.649404 )
							if( ma20 <= 0.612844 )
								ret := -0.250000
							if( ma20 > 0.612844 )
								ret := -1.000000 // sell
						if( ma05 > 0.649404 )
							if( ma90 <= 4.05885 )
								if( ma100 <= 3.94365 )
									ret := -0.032568
								if( ma100 > 3.94365 )
									ret := 0.588235
							if( ma90 > 4.05885 )
								if( ma90_colorInt <= 2.5 )
									ret := 0.642857
								if( ma90_colorInt > 2.5 )
									ret := -0.687500
					if( ma15 > 4.33272 )
						if( ma10 <= 4.56121 )
							if( ma90_colorInt <= 2.5 )
								ret := -0.500000
							if( ma90_colorInt > 2.5 )
								if( ma55 <= 4.58855 )
									ret := 1.000000 // buy
								if( ma55 > 4.58855 )
									ret := 0.750000 // buy
						if( ma10 > 4.56121 )
							if( ma20 <= 5.19669 )
								if( ma20 <= 4.72082 )
									ret := 0.272727
								if( ma20 > 4.72082 )
									ret := -0.139535
							if( ma20 > 5.19669 )
								if( ma90 <= 5.63232 )
									ret := 0.458333
								if( ma90 > 5.63232 )
									ret := -0.137931
			if( ma100 > 5.76279 )
				if( ma05 <= 5.65239 )
					if( ma85 <= 5.80201 )
						if( ma65 <= 5.65237 )
							ret := -0.833333 // sell
						if( ma65 > 5.65237 )
							if( ma05 <= 5.30643 )
								ret := 0.750000 // buy
							if( ma05 > 5.30643 )
								if( ma25 <= 5.6745 )
									ret := -0.263158
								if( ma25 > 5.6745 )
									ret := 0.125000
					if( ma85 > 5.80201 )
						if( ma15 <= 5.64688 )
							if( ma80 <= 5.85456 )
								ret := -0.666667
							if( ma80 > 5.85456 )
								ret := -1.000000 // sell
						if( ma15 > 5.64688 )
							if( ma65 <= 5.83662 )
								if( ma15 <= 5.68929 )
									ret := -0.750000 // sell
								if( ma15 > 5.68929 )
									ret := -1.000000 // sell
							if( ma65 > 5.83662 )
								if( ma25 <= 5.74839 )
									ret := 0.250000
								if( ma25 > 5.74839 )
									ret := -0.727273 // sell
				if( ma05 > 5.65239 )
					if( ma75 <= 39.7731 )
						if( ma70 <= 38.9747 )
							if( ma20_colorInt <= 2.5 )
								if( ma90_colorInt <= 1.5 )
									ret := 0.113407
								if( ma90_colorInt > 1.5 )
									ret := 0.198566
							if( ma20_colorInt > 2.5 )
								if( ma100 <= 17.5474 )
									ret := 0.106311
								if( ma100 > 17.5474 )
									ret := 0.010532
						if( ma70 > 38.9747 )
							if( ma50 <= 38.9347 )
								if( ma100 <= 40.291 )
									ret := 0.888889 // buy
								if( ma100 > 40.291 )
									ret := 0.166667
							if( ma50 > 38.9347 )
								if( ma40 <= 39.5182 )
									ret := 0.082192
								if( ma40 > 39.5182 )
									ret := 0.723684 // buy
					if( ma75 > 39.7731 )
						if( ma80 <= 41.4131 )
							if( ma70 <= 40.7398 )
								if( ma50 <= 39.6489 )
									ret := -0.690476
								if( ma50 > 39.6489 )
									ret := -0.093023
							if( ma70 > 40.7398 )
								if( ma35 <= 41.6581 )
									ret := -0.807229 // sell
								if( ma35 > 41.6581 )
									ret := 0.240000
						if( ma80 > 41.4131 )
							if( ma100 <= 42.5069 )
								if( ma25_colorInt <= 1.5 )
									ret := -0.214286
								if( ma25_colorInt > 1.5 )
									ret := 0.623596
							if( ma100 > 42.5069 )
								if( ma10 <= 44.847 )
									ret := -0.132515
								if( ma10 > 44.847 )
									ret := 0.052458
	if( ma15_colorInt > 3.5 )
		if( ma90_colorInt <= 3.5 )
			if( ma10 <= 86.0416 )
				if( ma05 <= 75.5016 )
					if( ma65_colorInt <= 2.5 )
						if( ma35 <= 1.14675 )
							if( ma10_colorInt <= 2.5 )
								if( ma60 <= 0.885057 )
									ret := 0.500000
								if( ma60 > 0.885057 )
									ret := -0.250000
							if( ma10_colorInt > 2.5 )
								if( ma35_colorInt <= 1.5 )
									ret := -0.291667
								if( ma35_colorInt > 1.5 )
									ret := -0.632911
						if( ma35 > 1.14675 )
							if( ma45_colorInt <= 2.5 )
								if( ma85 <= 16.682 )
									ret := -0.006682
								if( ma85 > 16.682 )
									ret := -0.290076
							if( ma45_colorInt > 2.5 )
								if( ma90 <= 6.67589 )
									ret := -0.324675
								if( ma90 > 6.67589 )
									ret := -0.074534
					if( ma65_colorInt > 2.5 )
						if( ma05_colorInt <= 3.5 )
							if( ma45 <= 31.9001 )
								if( ma55 <= 27.3493 )
									ret := 0.125356
								if( ma55 > 27.3493 )
									ret := 0.916667 // buy
							if( ma45 > 31.9001 )
								if( ma30 <= 74.746 )
									ret := -0.060052
								if( ma30 > 74.746 )
									ret := -1.000000 // sell
						if( ma05_colorInt > 3.5 )
							if( ma100 <= 77.1097 )
								if( ma90 <= 58.088 )
									ret := -0.056394
								if( ma90 > 58.088 )
									ret := 0.061275
							if( ma100 > 77.1097 )
								if( ma05 <= 73.8763 )
									ret := 0.166667
								if( ma05 > 73.8763 )
									ret := -0.787234 // sell
				if( ma05 > 75.5016 )
					if( ma70 <= 79.188 )
						if( ma65 <= 78.6933 )
							if( ma60 <= 76.5552 )
								if( ma70 <= 75.4474 )
									ret := 0.250000
								if( ma70 > 75.4474 )
									ret := 1.000000 // buy
							if( ma60 > 76.5552 )
								if( ma25 <= 76.1134 )
									ret := -0.800000 // sell
								if( ma25 > 76.1134 )
									ret := -0.083333
						if( ma65 > 78.6933 )
							ret := 1.000000 // buy
					if( ma70 > 79.188 )
						if( ma70 <= 79.2267 )
							ret := -1.000000 // sell
						if( ma70 > 79.2267 )
							if( ma05 <= 82.946 )
								if( ma50_colorInt <= 3.5 )
									ret := -0.032787
								if( ma50_colorInt > 3.5 )
									ret := -0.625000
							if( ma05 > 82.946 )
								if( ma90 <= 83.2685 )
									ret := 1.000000 // buy
								if( ma90 > 83.2685 )
									ret := 0.166667
			if( ma10 > 86.0416 )
				if( ma45 <= 86.7319 )
					if( ma80 <= 87.0947 )
						ret := -1.000000 // sell
					if( ma80 > 87.0947 )
						ret := -0.750000 // sell
				if( ma45 > 86.7319 )
					if( ma85 <= 89.7261 )
						if( ma15 <= 86.6184 )
							ret := 0.250000
						if( ma15 > 86.6184 )
							if( ma55 <= 89.4262 )
								ret := 0.000000
							if( ma55 > 89.4262 )
								ret := -0.250000
					if( ma85 > 89.7261 )
						if( ma50 <= 90.3231 )
							if( ma10 <= 86.6636 )
								ret := -0.500000
							if( ma10 > 86.6636 )
								ret := -1.000000 // sell
						if( ma50 > 90.3231 )
							ret := 0.000000
		if( ma90_colorInt > 3.5 )
			if( ma05_colorInt <= 3.5 )
				if( ma25 <= 1.44548 )
					if( ma55 <= 1.44117 )
						if( ma70 <= 0.785491 )
							if( ma75 <= 0.685218 )
								ret := -0.200000
							if( ma75 > 0.685218 )
								if( ma50 <= 0.69505 )
									ret := -1.000000 // sell
								if( ma50 > 0.69505 )
									ret := -0.700000 // sell
						if( ma70 > 0.785491 )
							if( ma45 <= 0.923614 )
								if( ma05 <= 0.906276 )
									ret := -0.100000
								if( ma05 > 0.906276 )
									ret := 0.750000 // buy
							if( ma45 > 0.923614 )
								if( ma90 <= 0.928352 )
									ret := -1.000000 // sell
								if( ma90 > 0.928352 )
									ret := -0.181347
					if( ma55 > 1.44117 )
						if( ma100 <= 1.45096 )
							ret := -1.000000 // sell
						if( ma100 > 1.45096 )
							ret := -0.714286 // sell
				if( ma25 > 1.44548 )
					if( ma10 <= 1.62174 )
						if( ma05 <= 1.62866 )
							if( ma05_colorInt <= 1.5 )
								if( ma65 <= 1.47317 )
									ret := 0.647059
								if( ma65 > 1.47317 )
									ret := 0.281250
							if( ma05_colorInt > 1.5 )
								if( ma45 <= 1.51722 )
									ret := 0.500000
								if( ma45 > 1.51722 )
									ret := 1.000000 // buy
						if( ma05 > 1.62866 )
							ret := 1.000000 // buy
					if( ma10 > 1.62174 )
						if( ma65 <= 85.609 )
							if( ma100 <= 76.9823 )
								if( ma100 <= 74.7987 )
									ret := -0.020101
								if( ma100 > 74.7987 )
									ret := -0.882353 // sell
							if( ma100 > 76.9823 )
								if( ma90 <= 85.231 )
									ret := 0.689655
								if( ma90 > 85.231 )
									ret := -0.071429
						if( ma65 > 85.609 )
							if( ma85 <= 87.859 )
								ret := -1.000000 // sell
							if( ma85 > 87.859 )
								ret := -0.833333 // sell
			if( ma05_colorInt > 3.5 )
				if( ma25 <= 23.5143 )
					if( ma20 <= 1.00708 )
						if( ma75 <= 0.643861 )
							ret := 1.000000 // buy
						if( ma75 > 0.643861 )
							if( ma90 <= 0.67403 )
								if( ma60 <= 0.650478 )
									ret := -1.000000 // sell
								if( ma60 > 0.650478 )
									ret := 0.500000
							if( ma90 > 0.67403 )
								if( ma20 <= 0.701705 )
									ret := -0.827586 // sell
								if( ma20 > 0.701705 )
									ret := -0.637931
					if( ma20 > 1.00708 )
						if( ma30 <= 1.45487 )
							if( ma10 <= 1.43111 )
								if( ma05 <= 1.35084 )
									ret := 0.174312
								if( ma05 > 1.35084 )
									ret := -0.272727
							if( ma10 > 1.43111 )
								if( ma90 <= 1.44656 )
									ret := 1.000000 // buy
								if( ma90 > 1.44656 )
									ret := 0.375000
						if( ma30 > 1.45487 )
							if( ma15 <= 1.55896 )
								if( ma100 <= 1.48271 )
									ret := -0.925926 // sell
								if( ma100 > 1.48271 )
									ret := -0.666667
							if( ma15 > 1.55896 )
								if( ma70 <= 1.69293 )
									ret := 0.270833
								if( ma70 > 1.69293 )
									ret := -0.372408
				if( ma25 > 23.5143 )
					if( ma60 <= 32.0736 )
						if( ma100 <= 25.8728 )
							if( ma90 <= 23.8783 )
								ret := 0.857143 // buy
							if( ma90 > 23.8783 )
								if( ma55 <= 24.7939 )
									ret := -0.200000
								if( ma55 > 24.7939 )
									ret := -1.000000 // sell
						if( ma100 > 25.8728 )
							if( ma10 <= 32.0298 )
								if( ma75 <= 32.049 )
									ret := 0.703704 // buy
								if( ma75 > 32.049 )
									ret := -0.285714
							if( ma10 > 32.0298 )
								ret := 1.000000 // buy
					if( ma60 > 32.0736 )
						if( ma20 <= 32.6332 )
							if( ma100 <= 32.3984 )
								ret := -0.250000
							if( ma100 > 32.3984 )
								ret := -1.000000 // sell
						if( ma20 > 32.6332 )
							if( ma65 <= 86.4602 )
								if( ma30 <= 63.2486 )
									ret := -0.090047
								if( ma30 > 63.2486 )
									ret := 0.092784
							if( ma65 > 86.4602 )
								ret := -0.857143 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Madrid_Moving_Average_Ribbon 
//@version=5
//indicator "Madrid Moving Average Ribbon", shorttitle="Madrid Ribbon", overlay=true)


PHI     = (1 + math.sqrt(5)) / 2
PI      = 104348 / 33215

BULL    = 1
BEAR    = -1
NONE    = 0

GRN01 = color.rgb(124, 252, 0)
GRN02 = color.rgb(50, 205, 50)
GRN03 = color.rgb(34, 139, 34)
GRN04 = color.rgb(0, 100, 0)
GRN05 = color.rgb(0, 128, 0)
GRN06 = color.rgb(9, 53, 7)
RED01 = color.rgb(255, 69, 0)
RED02 = color.rgb(255, 0, 0)
RED03 = color.rgb(178, 34, 34)
RED04 = color.rgb(139, 0, 0)
RED05 = color.rgb(128, 0, 0)
RED06 = color.rgb(51, 13, 6)

// Define other v3 Style Colors
AQUA    = color.rgb(0, 255, 255)
BLACK   = color.rgb(0, 0, 0)
BLUE    = color.rgb(0, 0, 255)
FUCHSIA = color.rgb(255, 0, 255)
GRAY    = color.rgb(128, 128, 128)
GREEN   = color.rgb(0, 128, 0)
LIME    = color.rgb(0, 255, 0)
MAROON  = color.rgb(128, 0, 0)
NAVY    = color.rgb(0, 0, 128)
OLIVE   = color.rgb(128, 128, 0)
ORANGE  = color.rgb(255, 127, 0)
PURPLE  = color.rgb(128, 0, 128)
RUBI    = color.rgb(255, 0, 0)
SILVER  = color.rgb(192, 192, 192)
TEAL    = color.rgb(0, 128, 128)
YELLOW  = color.rgb(255, 255, 0)
WHITE   = color.rgb(255, 255, 255)


// ──────────[ Moving Average Color ]
maColor(_ma, _maRef) =>
    diffMA = ta.change(_ma)
    diffMA >= 0 and _ma > _maRef ? LIME : diffMA < 0 and _ma > _maRef ? MAROON : diffMA <= 0 and _ma < _maRef ? RUBI : diffMA >= 0 and _ma < _maRef ? GREEN : GRAY

// Function to calculate the integer representing the color condition
ma_color_int(ma, ma_ref) =>
    diff_ma = ta.change(ma)
    diff_ma >= 0 and ma > ma_ref ? 1 : diff_ma < 0 and ma > ma_ref ? 2 : diff_ma <= 0 and ma < ma_ref ? 3 : diff_ma >= 0 and ma < ma_ref ? 4 : 5


_10   = input.bool(false, '───────────[ Madrid Ribbon]───────────' )
i_exp = input(true, title="Exponential MA")

// ────────────────────[ Processing ]
src = close

ma05  = i_exp ? ta.ema(src, 5) : ta.sma(src, 5)
ma10  = i_exp ? ta.ema(src, 10) : ta.sma(src, 10)
ma15  = i_exp ? ta.ema(src, 15) : ta.sma(src, 15)
ma20  = i_exp ? ta.ema(src, 20) : ta.sma(src, 20)
ma25  = i_exp ? ta.ema(src, 25) : ta.sma(src, 25)
ma30  = i_exp ? ta.ema(src, 30) : ta.sma(src, 30)
ma35  = i_exp ? ta.ema(src, 35) : ta.sma(src, 35)
ma40  = i_exp ? ta.ema(src, 40) : ta.sma(src, 40)
ma45  = i_exp ? ta.ema(src, 45) : ta.sma(src, 45)
ma50  = i_exp ? ta.ema(src, 50) : ta.sma(src, 50)
ma55  = i_exp ? ta.ema(src, 55) : ta.sma(src, 55)
ma60  = i_exp ? ta.ema(src, 60) : ta.sma(src, 60)
ma65  = i_exp ? ta.ema(src, 65) : ta.sma(src, 65)
ma70  = i_exp ? ta.ema(src, 70) : ta.sma(src, 70)
ma75  = i_exp ? ta.ema(src, 75) : ta.sma(src, 75)
ma80  = i_exp ? ta.ema(src, 80) : ta.sma(src, 80)
ma85  = i_exp ? ta.ema(src, 85) : ta.sma(src, 85)
ma90  = i_exp ? ta.ema(src, 90) : ta.sma(src, 90)
ma100 = i_exp ? ta.ema(src, 100) : ta.sma(src, 100)

// ────────────────────[ Plot ]
plot(ma05, color=maColor(ma05, ma100), title="MMA05", linewidth=3)
plot(ma10, color=maColor(ma10, ma100), title="MMA10", linewidth=1)
plot(ma15, color=maColor(ma15, ma100), title="MMA15", linewidth=1)
plot(ma20, color=maColor(ma20, ma100), title="MMA20", linewidth=1)
plot(ma25, color=maColor(ma25, ma100), title="MMA25", linewidth=1)
plot(ma30, color=maColor(ma30, ma100), title="MMA30", linewidth=1)
plot(ma35, color=maColor(ma35, ma100), title="MMA35", linewidth=1)
plot(ma40, color=maColor(ma40, ma100), title="MMA40", linewidth=1)
plot(ma45, color=maColor(ma45, ma100), title="MMA45", linewidth=1)
plot(ma50, color=maColor(ma50, ma100), title="MMA50", linewidth=1)
plot(ma55, color=maColor(ma55, ma100), title="MMA55", linewidth=1)
plot(ma60, color=maColor(ma60, ma100), title="MMA60", linewidth=1)
plot(ma65, color=maColor(ma65, ma100), title="MMA65", linewidth=1)
plot(ma70, color=maColor(ma70, ma100), title="MMA70", linewidth=1)
plot(ma75, color=maColor(ma75, ma100), title="MMA75", linewidth=1)
plot(ma80, color=maColor(ma80, ma100), title="MMA80", linewidth=1)
plot(ma85, color=maColor(ma85, ma100), title="MMA85", linewidth=1)
plot(ma90, color=maColor(ma90, ma100), title="MMA90", linewidth=3)



//Calculate colors based on the moving averages compared to ma100
ma05_colorInt = ma_color_int(ma05, ma100)
ma10_colorInt = ma_color_int(ma10, ma100)
ma15_colorInt = ma_color_int(ma15, ma100)
ma20_colorInt = ma_color_int(ma20, ma100)
ma25_colorInt = ma_color_int(ma25, ma100)
ma30_colorInt = ma_color_int(ma30, ma100)
ma35_colorInt = ma_color_int(ma35, ma100)
ma40_colorInt = ma_color_int(ma40, ma100)
ma45_colorInt = ma_color_int(ma45, ma100)
ma50_colorInt = ma_color_int(ma50, ma100)
ma55_colorInt = ma_color_int(ma55, ma100)
ma60_colorInt = ma_color_int(ma60, ma100)
ma65_colorInt = ma_color_int(ma65, ma100)
ma70_colorInt = ma_color_int(ma70, ma100)
ma75_colorInt = ma_color_int(ma75, ma100)
ma80_colorInt = ma_color_int(ma80, ma100)
ma85_colorInt = ma_color_int(ma85, ma100)
ma90_colorInt = ma_color_int(ma90, ma100)


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
float op_operation = decision_tree_0_APPS_15Min_43d49d1f(ma65, ma15_colorInt, ma90_colorInt, ma75, ma10_colorInt, ma100, ma65_colorInt, ma50, ma55_colorInt, ma80_colorInt, ma70, ma20, ma30_colorInt, ma60, ma05, ma25, ma60_colorInt, ma35, ma25_colorInt, ma05_colorInt, ma90, ma80, ma40_colorInt, ma85, ma75_colorInt, ma30, ma40, ma55, ma15, ma35_colorInt, ma70_colorInt, ma45, ma20_colorInt, ma10, ma45_colorInt, ma85_colorInt, ma50_colorInt)

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


