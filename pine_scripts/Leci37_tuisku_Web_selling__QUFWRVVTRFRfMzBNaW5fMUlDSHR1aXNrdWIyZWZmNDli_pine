//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ichimoku_Cloud
// ID_model: AAVEUSDT_30Min_1ICH_b2eff49b Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAVEUSDT_30Min_1ICH_b2eff49b", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAVEUSDT_30Min_b2eff49b(basis_max, tenkan_sen, senkou_span_b, senkou_span_b_displaced, kinjun_sen, senkou_span_a, chinkou_span, basis_minus, cross_dn_tenkan_kinjunInt, senkou_span_a_displaced, cross_up_tenkan_kinjunInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( senkou_span_b <= 373.746 )
		if( chinkou_span <= 331.807 )
			if( senkou_span_a <= 323.028 )
				if( tenkan_sen <= 83.947 )
					if( kinjun_sen <= 83.4925 )
						if( basis_minus <= 2.21572 )
							if( chinkou_span <= 81.9555 )
								if( senkou_span_b <= 76.352 )
									ret := 0.039221
								if( senkou_span_b > 76.352 )
									ret := -0.140277
							if( chinkou_span > 81.9555 )
								if( chinkou_span <= 84.5405 )
									ret := 0.264531
								if( chinkou_span > 84.5405 )
									ret := 0.553909
						if( basis_minus > 2.21572 )
							if( senkou_span_b_displaced <= 56.1112 )
								if( senkou_span_a_displaced <= 56.0138 )
									ret := 0.156352
								if( senkou_span_a_displaced > 56.0138 )
									ret := 0.893333 // buy
							if( senkou_span_b_displaced > 56.1112 )
								if( senkou_span_a_displaced <= 75.1967 )
									ret := -0.277778
								if( senkou_span_a_displaced > 75.1967 )
									ret := 0.102767
					if( kinjun_sen > 83.4925 )
						if( chinkou_span <= 81.5431 )
							if( kinjun_sen <= 90.8982 )
								if( basis_minus <= -3.07694 )
									ret := -0.938776 // sell
								if( basis_minus > -3.07694 )
									ret := -0.057348
							if( kinjun_sen > 90.8982 )
								ret := 1.000000 // buy
						if( chinkou_span > 81.5431 )
							if( kinjun_sen <= 85.0097 )
								if( tenkan_sen <= 82.0991 )
									ret := 0.781250 // buy
								if( tenkan_sen > 82.0991 )
									ret := 0.533428
							if( kinjun_sen > 85.0097 )
								if( senkou_span_b_displaced <= 90.295 )
									ret := -0.584906
								if( senkou_span_b_displaced > 90.295 )
									ret := 0.233333
				if( tenkan_sen > 83.947 )
					if( senkou_span_b_displaced <= 358.15 )
						if( basis_max <= 2.55267 )
							if( chinkou_span <= 88.001 )
								if( senkou_span_a <= 89.2761 )
									ret := -0.218514
								if( senkou_span_a > 89.2761 )
									ret := -0.608868
							if( chinkou_span > 88.001 )
								if( senkou_span_b <= 90.0477 )
									ret := 0.332916
								if( senkou_span_b > 90.0477 )
									ret := -0.014738
						if( basis_max > 2.55267 )
							if( kinjun_sen <= 200.923 )
								if( chinkou_span <= 177.266 )
									ret := 0.220751
								if( chinkou_span > 177.266 )
									ret := 0.763736 // buy
							if( kinjun_sen > 200.923 )
								if( senkou_span_a_displaced <= 218.651 )
									ret := -0.822430 // sell
								if( senkou_span_a_displaced > 218.651 )
									ret := 0.079452
					if( senkou_span_b_displaced > 358.15 )
						ret := 1.000000 // buy
			if( senkou_span_a > 323.028 )
				if( basis_minus <= -10.0901 )
					if( senkou_span_b <= 350.328 )
						if( senkou_span_b <= 341.924 )
							if( senkou_span_a_displaced <= 342.073 )
								ret := -0.200000
							if( senkou_span_a_displaced > 342.073 )
								ret := -1.000000 // sell
						if( senkou_span_b > 341.924 )
							if( kinjun_sen <= 335.64 )
								if( tenkan_sen <= 319.738 )
									ret := 0.500000
								if( tenkan_sen > 319.738 )
									ret := 0.680000
							if( kinjun_sen > 335.64 )
								if( kinjun_sen <= 340.226 )
									ret := 1.000000 // buy
								if( kinjun_sen > 340.226 )
									ret := 0.928571 // buy
					if( senkou_span_b > 350.328 )
						if( chinkou_span <= 320.859 )
							if( basis_max <= 9.1087 )
								ret := -1.000000 // sell
							if( basis_max > 9.1087 )
								ret := -0.636364
						if( chinkou_span > 320.859 )
							if( senkou_span_b_displaced <= 363.473 )
								if( senkou_span_a <= 331.004 )
									ret := 1.000000 // buy
								if( senkou_span_a > 331.004 )
									ret := 0.000000
							if( senkou_span_b_displaced > 363.473 )
								if( kinjun_sen <= 344.988 )
									ret := -0.750000 // sell
								if( kinjun_sen > 344.988 )
									ret := 0.161290
				if( basis_minus > -10.0901 )
					if( kinjun_sen <= 337.51 )
						if( senkou_span_b <= 303.747 )
							if( chinkou_span <= 303.67 )
								ret := 1.000000 // buy
							if( chinkou_span > 303.67 )
								ret := 0.750000 // buy
						if( senkou_span_b > 303.747 )
							if( senkou_span_b_displaced <= 310.909 )
								if( chinkou_span <= 325.523 )
									ret := -0.904348 // sell
								if( chinkou_span > 325.523 )
									ret := -0.400000
							if( senkou_span_b_displaced > 310.909 )
								if( basis_minus <= -7.89842 )
									ret := -0.884615 // sell
								if( basis_minus > -7.89842 )
									ret := -0.330619
					if( kinjun_sen > 337.51 )
						if( senkou_span_b_displaced <= 325.85 )
							ret := 0.250000
						if( senkou_span_b_displaced > 325.85 )
							if( senkou_span_a <= 339.418 )
								if( senkou_span_a <= 338.964 )
									ret := -0.670732
								if( senkou_span_a > 338.964 )
									ret := -0.125000
							if( senkou_span_a > 339.418 )
								if( senkou_span_b <= 360.418 )
									ret := -0.785185 // sell
								if( senkou_span_b > 360.418 )
									ret := -0.952830 // sell
		if( chinkou_span > 331.807 )
			if( senkou_span_a <= 362.891 )
				if( senkou_span_b_displaced <= 319.12 )
					if( kinjun_sen <= 321.864 )
						if( basis_minus <= 2.109 )
							if( senkou_span_b <= 279.34 )
								if( basis_max <= 0.144972 )
									ret := 0.571429
								if( basis_max > 0.144972 )
									ret := 1.000000 // buy
							if( senkou_span_b > 279.34 )
								if( senkou_span_b_displaced <= 314.989 )
									ret := 0.979310 // buy
								if( senkou_span_b_displaced > 314.989 )
									ret := 0.820000 // buy
						if( basis_minus > 2.109 )
							if( senkou_span_b_displaced <= 296.424 )
								if( basis_minus <= 15.9452 )
									ret := 0.962963 // buy
								if( basis_minus > 15.9452 )
									ret := 0.555556
							if( senkou_span_b_displaced > 296.424 )
								if( senkou_span_a <= 319.385 )
									ret := -0.076923
								if( senkou_span_a > 319.385 )
									ret := 0.588235
					if( kinjun_sen > 321.864 )
						if( basis_minus <= 16.6561 )
							if( senkou_span_a <= 327.902 )
								ret := -0.083333
							if( senkou_span_a > 327.902 )
								if( senkou_span_b_displaced <= 300.635 )
									ret := 0.931818 // buy
								if( senkou_span_b_displaced > 300.635 )
									ret := 0.721649 // buy
						if( basis_minus > 16.6561 )
							if( tenkan_sen <= 341 )
								if( tenkan_sen <= 330.262 )
									ret := -0.800000 // sell
								if( tenkan_sen > 330.262 )
									ret := -1.000000 // sell
							if( tenkan_sen > 341 )
								if( basis_max <= -9.17613 )
									ret := 1.000000 // buy
								if( basis_max > -9.17613 )
									ret := 0.062500
				if( senkou_span_b_displaced > 319.12 )
					if( senkou_span_a_displaced <= 381.556 )
						if( chinkou_span <= 354.406 )
							if( senkou_span_a <= 337.46 )
								if( senkou_span_a_displaced <= 333.161 )
									ret := 0.485876
								if( senkou_span_a_displaced > 333.161 )
									ret := -0.004926
							if( senkou_span_a > 337.46 )
								if( kinjun_sen <= 337.734 )
									ret := -0.884615 // sell
								if( kinjun_sen > 337.734 )
									ret := -0.156695
						if( chinkou_span > 354.406 )
							if( basis_max <= -11.9897 )
								if( tenkan_sen <= 366.499 )
									ret := -0.800000 // sell
								if( tenkan_sen > 366.499 )
									ret := -0.894737 // sell
							if( basis_max > -11.9897 )
								if( kinjun_sen <= 361.734 )
									ret := 0.481553
								if( kinjun_sen > 361.734 )
									ret := 0.894737 // buy
					if( senkou_span_a_displaced > 381.556 )
						if( senkou_span_a_displaced <= 389.537 )
							if( senkou_span_b <= 370.717 )
								if( tenkan_sen <= 326.404 )
									ret := 0.555556
								if( tenkan_sen > 326.404 )
									ret := -0.793103 // sell
							if( senkou_span_b > 370.717 )
								ret := 0.454545
						if( senkou_span_a_displaced > 389.537 )
							if( senkou_span_a_displaced <= 407.016 )
								if( senkou_span_b <= 361.664 )
									ret := 0.457143
								if( senkou_span_b > 361.664 )
									ret := -0.636364
							if( senkou_span_a_displaced > 407.016 )
								if( chinkou_span <= 380.664 )
									ret := 0.900000 // buy
								if( chinkou_span > 380.664 )
									ret := 0.133333
			if( senkou_span_a > 362.891 )
				if( senkou_span_b <= 366.924 )
					if( chinkou_span <= 414.584 )
						if( kinjun_sen <= 381.511 )
							if( basis_max <= -0.022045 )
								if( basis_max <= -9.11624 )
									ret := 0.307692
								if( basis_max > -9.11624 )
									ret := -0.258475
							if( basis_max > -0.022045 )
								if( chinkou_span <= 338.165 )
									ret := -0.937500 // sell
								if( chinkou_span > 338.165 )
									ret := 0.331731
						if( kinjun_sen > 381.511 )
							if( basis_max <= -2.39509 )
								ret := -0.111111
							if( basis_max > -2.39509 )
								if( senkou_span_b_displaced <= 356.191 )
									ret := -0.854839 // sell
								if( senkou_span_b_displaced > 356.191 )
									ret := -0.454545
					if( chinkou_span > 414.584 )
						if( senkou_span_a <= 395.571 )
							ret := 0.842105 // buy
						if( senkou_span_a > 395.571 )
							ret := 0.727273 // buy
				if( senkou_span_b > 366.924 )
					if( chinkou_span <= 382.358 )
						if( senkou_span_a <= 363.949 )
							if( chinkou_span <= 369.645 )
								ret := -0.428571
							if( chinkou_span > 369.645 )
								ret := -1.000000 // sell
						if( senkou_span_a > 363.949 )
							if( kinjun_sen <= 377.884 )
								if( basis_minus <= 5.36362 )
									ret := -0.034965
								if( basis_minus > 5.36362 )
									ret := 0.593407
							if( kinjun_sen > 377.884 )
								if( chinkou_span <= 381.231 )
									ret := -0.295775
								if( chinkou_span > 381.231 )
									ret := -0.941176 // sell
					if( chinkou_span > 382.358 )
						if( senkou_span_b <= 368.492 )
							if( senkou_span_b <= 367.674 )
								if( basis_max <= 0.063241 )
									ret := 0.250000
								if( basis_max > 0.063241 )
									ret := 0.724138 // buy
							if( senkou_span_b > 367.674 )
								if( basis_max <= -0.271146 )
									ret := -0.321429
								if( basis_max > -0.271146 )
									ret := 0.857143 // buy
						if( senkou_span_b > 368.492 )
							if( senkou_span_a_displaced <= 371.151 )
								if( senkou_span_a_displaced <= 370.261 )
									ret := 0.576923
								if( senkou_span_a_displaced > 370.261 )
									ret := -0.312500
							if( senkou_span_a_displaced > 371.151 )
								if( senkou_span_b_displaced <= 370.267 )
									ret := 0.948276 // buy
								if( senkou_span_b_displaced > 370.267 )
									ret := 0.000000
	if( senkou_span_b > 373.746 )
		if( senkou_span_a <= 340.624 )
			if( senkou_span_b_displaced <= 396.789 )
				if( kinjun_sen <= 333.867 )
					if( tenkan_sen <= 324.825 )
						ret := 1.000000 // buy
					if( tenkan_sen > 324.825 )
						ret := 0.909091 // buy
				if( kinjun_sen > 333.867 )
					ret := 0.000000
			if( senkou_span_b_displaced > 396.789 )
				ret := 1.000000 // buy
		if( senkou_span_a > 340.624 )
			if( chinkou_span <= 386.135 )
				if( tenkan_sen <= 388.132 )
					if( chinkou_span <= 366.944 )
						if( senkou_span_b_displaced <= 426.655 )
							if( senkou_span_b <= 376.085 )
								if( chinkou_span <= 328.745 )
									ret := 0.529412
								if( chinkou_span > 328.745 )
									ret := -0.361446
							if( senkou_span_b > 376.085 )
								if( basis_minus <= -6.42098 )
									ret := -0.735023 // sell
								if( basis_minus > -6.42098 )
									ret := -0.463415
						if( senkou_span_b_displaced > 426.655 )
							if( chinkou_span <= 339.8 )
								if( senkou_span_b_displaced <= 434.835 )
									ret := 0.500000
								if( senkou_span_b_displaced > 434.835 )
									ret := -1.000000 // sell
							if( chinkou_span > 339.8 )
								if( senkou_span_a_displaced <= 458.323 )
									ret := 0.081081
								if( senkou_span_a_displaced > 458.323 )
									ret := 1.000000 // buy
					if( chinkou_span > 366.944 )
						if( kinjun_sen <= 376.9 )
							if( senkou_span_b <= 374.921 )
								if( tenkan_sen <= 370.272 )
									ret := -0.300000
								if( tenkan_sen > 370.272 )
									ret := -0.818182 // sell
							if( senkou_span_b > 374.921 )
								if( senkou_span_b <= 377.858 )
									ret := 0.392405
								if( senkou_span_b > 377.858 )
									ret := 0.800000 // buy
						if( kinjun_sen > 376.9 )
							if( senkou_span_b <= 392.242 )
								if( tenkan_sen <= 384.541 )
									ret := -0.371747
								if( tenkan_sen > 384.541 )
									ret := 0.448276
							if( senkou_span_b > 392.242 )
								if( kinjun_sen <= 392.283 )
									ret := 0.417722
								if( kinjun_sen > 392.283 )
									ret := -0.708333 // sell
				if( tenkan_sen > 388.132 )
					if( basis_max <= -0.9475 )
						if( chinkou_span <= 385.074 )
							if( senkou_span_b_displaced <= 360.47 )
								ret := -1.000000 // sell
							if( senkou_span_b_displaced > 360.47 )
								if( senkou_span_b_displaced <= 387.673 )
									ret := -0.839286 // sell
								if( senkou_span_b_displaced > 387.673 )
									ret := -0.940299 // sell
						if( chinkou_span > 385.074 )
							ret := -0.538462
					if( basis_max > -0.9475 )
						if( senkou_span_b <= 400.859 )
							if( senkou_span_b_displaced <= 400.3 )
								if( senkou_span_b_displaced <= 397.352 )
									ret := -0.543860
								if( senkou_span_b_displaced > 397.352 )
									ret := 0.731707 // buy
							if( senkou_span_b_displaced > 400.3 )
								if( senkou_span_b <= 398.416 )
									ret := -0.901639 // sell
								if( senkou_span_b > 398.416 )
									ret := 0.090909
						if( senkou_span_b > 400.859 )
							if( senkou_span_b_displaced <= 435.572 )
								if( senkou_span_a_displaced <= 407.835 )
									ret := -0.557377
								if( senkou_span_a_displaced > 407.835 )
									ret := -0.878049 // sell
							if( senkou_span_b_displaced > 435.572 )
								if( basis_minus <= -8.09166 )
									ret := -0.835443 // sell
								if( basis_minus > -8.09166 )
									ret := 0.315789
			if( chinkou_span > 386.135 )
				if( kinjun_sen <= 395.438 )
					if( basis_minus <= 1.59106 )
						if( basis_max <= -0.407 )
							if( senkou_span_a_displaced <= 399.453 )
								if( basis_minus <= 0.83375 )
									ret := 0.937500 // buy
								if( basis_minus > 0.83375 )
									ret := 0.533333
							if( senkou_span_a_displaced > 399.453 )
								if( senkou_span_b <= 397.271 )
									ret := 0.842105 // buy
								if( senkou_span_b > 397.271 )
									ret := 0.200000
						if( basis_max > -0.407 )
							if( kinjun_sen <= 384.863 )
								if( senkou_span_a_displaced <= 383.756 )
									ret := 0.614035
								if( senkou_span_a_displaced > 383.756 )
									ret := -0.230769
							if( kinjun_sen > 384.863 )
								if( basis_max <= 3.65875 )
									ret := 0.807229 // buy
								if( basis_max > 3.65875 )
									ret := 0.333333
					if( basis_minus > 1.59106 )
						if( senkou_span_b_displaced <= 366.132 )
							if( chinkou_span <= 391.99 )
								ret := 0.777778 // buy
							if( chinkou_span > 391.99 )
								if( senkou_span_b <= 376.651 )
									ret := 0.365854
								if( senkou_span_b > 376.651 )
									ret := -0.465116
						if( senkou_span_b_displaced > 366.132 )
							if( senkou_span_a_displaced <= 382.901 )
								if( senkou_span_a <= 384.545 )
									ret := 0.076923
								if( senkou_span_a > 384.545 )
									ret := 0.531250
							if( senkou_span_a_displaced > 382.901 )
								if( chinkou_span <= 411.253 )
									ret := 0.607143
								if( chinkou_span > 411.253 )
									ret := 0.903846 // buy
				if( kinjun_sen > 395.438 )
					if( basis_minus <= -12.5938 )
						if( tenkan_sen <= 432.923 )
							if( senkou_span_b <= 446.879 )
								if( senkou_span_b <= 443.574 )
									ret := 0.915493 // buy
								if( senkou_span_b > 443.574 )
									ret := -0.500000
							if( senkou_span_b > 446.879 )
								ret := 1.000000 // buy
						if( tenkan_sen > 432.923 )
							if( senkou_span_b <= 470.863 )
								if( basis_minus <= -14.5224 )
									ret := -0.764706 // sell
								if( basis_minus > -14.5224 )
									ret := -0.222222
							if( senkou_span_b > 470.863 )
								if( senkou_span_a_displaced <= 561.319 )
									ret := 0.574913
								if( senkou_span_a_displaced > 561.319 )
									ret := -0.408537
					if( basis_minus > -12.5938 )
						if( senkou_span_a <= 458.441 )
							if( basis_minus <= 12.3072 )
								if( senkou_span_a_displaced <= 383.148 )
									ret := -0.734940 // sell
								if( senkou_span_a_displaced > 383.148 )
									ret := 0.002982
							if( basis_minus > 12.3072 )
								if( chinkou_span <= 422.066 )
									ret := -0.484211
								if( chinkou_span > 422.066 )
									ret := 0.655738
						if( senkou_span_a > 458.441 )
							if( senkou_span_a <= 480.396 )
								if( kinjun_sen <= 464.967 )
									ret := -0.275488
								if( kinjun_sen > 464.967 )
									ret := -0.584352
							if( senkou_span_a > 480.396 )
								if( senkou_span_b <= 498.587 )
									ret := 0.235023
								if( senkou_span_b > 498.587 )
									ret := -0.282588
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Ichimoku_Cloud 
//@version=5
//indicator "Ichimoku Cloud", overlay=true)

// Input parameters for the Ichimoku Cloud
turning_periods = input.int(9, title="Tenkan-Sen Period")
standard_periods = input.int(26, title="Kinjun-Sen Period")
leading_span2_periods = input.int(52, title="Senkou Span B Period")
displacement = input.int(26, title="Displacement")

show_tenkan_sen = input.bool(true, title="Show Tenkan-Sen")
show_kinjun_sen = input.bool(true, title="Show Kinjun-Sen")
show_chinkou_span = input.bool(true, title="Show Chinkou Span")
show_cloud = input.bool(true, title="Show Cloud")
show_crosses = input.bool(false, title="Show Crosses")

// Donchian channel calculation
donchian(highs, lows, length) =>
    (ta.highest(highs, length) + ta.lowest(lows, length)) / 2

// Ichimoku calculations
tenkan_sen = donchian(high, low, turning_periods)
kinjun_sen = donchian(high, low, standard_periods)
senkou_span_a = (tenkan_sen + kinjun_sen) / 2
senkou_span_b = donchian(high, low, leading_span2_periods)

// Displaced Senkou Spans
senkou_span_a_displaced = senkou_span_a[displacement]
senkou_span_b_displaced = senkou_span_b[displacement]

// Chinkou Span
chinkou_span = close[displacement]

// Crosses
cross_up_tenkan_kinjun = ta.crossover(tenkan_sen, kinjun_sen)
cross_dn_tenkan_kinjun = ta.crossunder(tenkan_sen, kinjun_sen)
cross_up_tenkan_kinjunInt = cross_up_tenkan_kinjun ? 1 : 0  // Bool to int
cross_dn_tenkan_kinjunInt = cross_dn_tenkan_kinjun ? 1 : 0  // Bool to int

basis_minus = senkou_span_a - senkou_span_b
basis_max = senkou_span_a - tenkan_sen

// Plotting
plot(show_tenkan_sen ? tenkan_sen : na, color=color.lime, title="Tenkan-Sen", linewidth=1)
plot(show_kinjun_sen ? kinjun_sen : na, color=color.fuchsia, title="Kinjun-Sen", linewidth=1)
plot(show_chinkou_span ? chinkou_span : na, color=color.aqua, title="Chinkou Span", linewidth=1, offset=-displacement)

// Plot the Senkou Span lines and store the plot references
senkou_span_a_plot = plot(show_cloud ? senkou_span_a_displaced : na, color=color.green, title="Senkou Span A", linewidth=1)
senkou_span_b_plot = plot(show_cloud ? senkou_span_b_displaced : na, color=color.red, title="Senkou Span B", linewidth=1)

// Cloud filling
fill(senkou_span_a_plot, senkou_span_b_plot, color=color.new(color.lime, 90), title="Bullish Cloud", transp=70, fillgaps=true)
fill(senkou_span_a_plot, senkou_span_b_plot, color=color.new(color.red, 90), title="Bearish Cloud", transp=70, fillgaps=true)

plotshape(series=(show_crosses and cross_up_tenkan_kinjun) ? close : na, location=location.belowbar, color=color.yellow, style=shape.triangleup, size=size.small, title="Cross Up Tenkan Kinjun")
plotshape(series=(show_crosses and cross_dn_tenkan_kinjun) ? close : na, location=location.abovebar, color=color.yellow, style=shape.triangledown, size=size.small, title="Cross Down Tenkan Kinjun")

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
float op_operation = decision_tree_0_AAVEUSDT_30Min_b2eff49b(basis_max, tenkan_sen, senkou_span_b, senkou_span_b_displaced, kinjun_sen, senkou_span_a, chinkou_span, basis_minus, cross_dn_tenkan_kinjunInt, senkou_span_a_displaced, cross_up_tenkan_kinjunInt)

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


