//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Madrid_Moving_Average_Ribbon
// ID_model: RIVN_5Min_1MAD_48622716 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RIVN_5Min_1MAD_48622716", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RIVN_5Min_48622716(ma05, ma50_colorInt, ma90, ma35_colorInt, ma90_colorInt, ma55_colorInt, ma20, ma15_colorInt, ma40_colorInt, ma45_colorInt, ma65_colorInt, ma75_colorInt, ma35, ma30, ma60, ma75, ma05_colorInt, ma45, ma40, ma30_colorInt, ma25, ma100, ma50, ma70_colorInt, ma10_colorInt, ma20_colorInt, ma60_colorInt, ma25_colorInt, ma10, ma15, ma80, ma65, ma85_colorInt, ma55, ma70, ma85, ma80_colorInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( ma85 <= 11.2829 )
		if( ma30_colorInt <= 3.5 )
			if( ma80 <= 11.2527 )
				if( ma50 <= 11.2866 )
					if( ma85 <= 8.6587 )
						if( ma85_colorInt <= 3.5 )
							if( ma75 <= 8.55537 )
								if( ma40 <= 8.41858 )
									ret := 0.769231 // buy
								if( ma40 > 8.41858 )
									ret := -0.531915
							if( ma75 > 8.55537 )
								if( ma25 <= 8.69408 )
									ret := 0.489712
								if( ma25 > 8.69408 )
									ret := 0.238095
						if( ma85_colorInt > 3.5 )
							if( ma90 <= 8.57642 )
								ret := 1.000000 // buy
							if( ma90 > 8.57642 )
								if( ma25 <= 8.62693 )
									ret := 0.100000
								if( ma25 > 8.62693 )
									ret := 0.826087 // buy
					if( ma85 > 8.6587 )
						if( ma35 <= 8.66391 )
							if( ma85 <= 8.70918 )
								if( ma80 <= 8.66404 )
									ret := -0.576923
								if( ma80 > 8.66404 )
									ret := -0.029412
							if( ma85 > 8.70918 )
								if( ma65 <= 8.69585 )
									ret := -0.545455
								if( ma65 > 8.69585 )
									ret := -0.948718 // sell
						if( ma35 > 8.66391 )
							if( ma10 <= 11.434 )
								if( ma05 <= 10.4411 )
									ret := 0.108263
								if( ma05 > 10.4411 )
									ret := 0.015236
							if( ma10 > 11.434 )
								ret := 1.000000 // buy
				if( ma50 > 11.2866 )
					if( ma20 <= 11.4869 )
						if( ma85 <= 11.2297 )
							ret := -0.111111
						if( ma85 > 11.2297 )
							if( ma10 <= 11.3686 )
								ret := -0.636364
							if( ma10 > 11.3686 )
								ret := -1.000000 // sell
					if( ma20 > 11.4869 )
						ret := -1.000000 // sell
			if( ma80 > 11.2527 )
				if( ma15 <= 11.6066 )
					if( ma10 <= 11.0475 )
						ret := -1.000000 // sell
					if( ma10 > 11.0475 )
						if( ma40 <= 11.3115 )
							if( ma90 <= 11.2505 )
								ret := 0.950000 // buy
							if( ma90 > 11.2505 )
								if( ma05 <= 11.1437 )
									ret := 0.886792 // buy
								if( ma05 > 11.1437 )
									ret := 0.401361
						if( ma40 > 11.3115 )
							if( ma60 <= 11.3308 )
								if( ma90 <= 11.2431 )
									ret := -0.727273 // sell
								if( ma90 > 11.2431 )
									ret := 0.157143
							if( ma60 > 11.3308 )
								ret := 1.000000 // buy
				if( ma15 > 11.6066 )
					ret := -1.000000 // sell
		if( ma30_colorInt > 3.5 )
			if( ma75 <= 10.8089 )
				if( ma100 <= 10.2271 )
					if( ma100 <= 10.1501 )
						if( ma25_colorInt <= 3.5 )
							if( ma50 <= 8.57746 )
								ret := -1.000000 // sell
							if( ma50 > 8.57746 )
								if( ma50 <= 10.0827 )
									ret := -0.593750
								if( ma50 > 10.0827 )
									ret := -0.285714
						if( ma25_colorInt > 3.5 )
							if( ma35_colorInt <= 3.5 )
								if( ma100 <= 9.24633 )
									ret := -0.704225 // sell
								if( ma100 > 9.24633 )
									ret := -0.095238
							if( ma35_colorInt > 3.5 )
								if( ma05_colorInt <= 1.5 )
									ret := 0.453125
								if( ma05_colorInt > 1.5 )
									ret := -0.119835
					if( ma100 > 10.1501 )
						if( ma30 <= 10.15 )
							if( ma65 <= 10.142 )
								if( ma05 <= 10.0684 )
									ret := 1.000000 // buy
								if( ma05 > 10.0684 )
									ret := 0.222222
							if( ma65 > 10.142 )
								if( ma65 <= 10.1552 )
									ret := 0.818182 // buy
								if( ma65 > 10.1552 )
									ret := 1.000000 // buy
						if( ma30 > 10.15 )
							if( ma60 <= 10.1809 )
								if( ma05_colorInt <= 1.5 )
									ret := -0.571429
								if( ma05_colorInt > 1.5 )
									ret := 0.115385
							if( ma60 > 10.1809 )
								if( ma30 <= 10.2025 )
									ret := 0.421875
								if( ma30 > 10.2025 )
									ret := 1.000000 // buy
				if( ma100 > 10.2271 )
					if( ma25 <= 10.2232 )
						if( ma25 <= 10.0596 )
							ret := 0.076923
						if( ma25 > 10.0596 )
							if( ma25 <= 10.1448 )
								ret := -1.000000 // sell
							if( ma25 > 10.1448 )
								if( ma25 <= 10.2076 )
									ret := -0.240964
								if( ma25 > 10.2076 )
									ret := -0.777778 // sell
					if( ma25 > 10.2232 )
						if( ma30 <= 10.418 )
							if( ma30 <= 10.2226 )
								ret := -1.000000 // sell
							if( ma30 > 10.2226 )
								if( ma90 <= 10.3532 )
									ret := -0.112948
								if( ma90 > 10.3532 )
									ret := -0.527174
						if( ma30 > 10.418 )
							if( ma60 <= 10.4791 )
								if( ma90 <= 10.479 )
									ret := 0.095238
								if( ma90 > 10.479 )
									ret := 0.744681 // buy
							if( ma60 > 10.4791 )
								if( ma10 <= 10.6208 )
									ret := -0.135802
								if( ma10 > 10.6208 )
									ret := -0.374194
			if( ma75 > 10.8089 )
				if( ma55_colorInt <= 3.5 )
					if( ma20 <= 11.1044 )
						if( ma40 <= 10.8065 )
							ret := 1.000000 // buy
						if( ma40 > 10.8065 )
							if( ma15 <= 10.8142 )
								ret := -0.400000
							if( ma15 > 10.8142 )
								if( ma10_colorInt <= 3.5 )
									ret := 0.883721 // buy
								if( ma10_colorInt > 3.5 )
									ret := 0.351351
					if( ma20 > 11.1044 )
						if( ma35 <= 11.1548 )
							if( ma25 <= 11.1206 )
								ret := 0.000000
							if( ma25 > 11.1206 )
								ret := -0.611111
						if( ma35 > 11.1548 )
							if( ma10 <= 11.1479 )
								ret := 1.000000 // buy
							if( ma10 > 11.1479 )
								if( ma90 <= 11.2374 )
									ret := 0.342105
								if( ma90 > 11.2374 )
									ret := -0.111111
				if( ma55_colorInt > 3.5 )
					if( ma60 <= 11.2714 )
						if( ma20_colorInt <= 2.5 )
							if( ma35 <= 10.8334 )
								ret := 0.545455
							if( ma35 > 10.8334 )
								if( ma40 <= 10.973 )
									ret := -0.176471
								if( ma40 > 10.973 )
									ret := -0.666667
						if( ma20_colorInt > 2.5 )
							if( ma10 <= 10.9523 )
								if( ma75 <= 10.9344 )
									ret := -0.067114
								if( ma75 > 10.9344 )
									ret := -0.733333 // sell
							if( ma10 > 10.9523 )
								if( ma85 <= 11.0335 )
									ret := 0.613208
								if( ma85 > 11.0335 )
									ret := 0.074534
					if( ma60 > 11.2714 )
						ret := 0.923077 // buy
	if( ma85 > 11.2829 )
		if( ma50_colorInt <= 3.5 )
			if( ma50 <= 25.8875 )
				if( ma100 <= 25.5702 )
					if( ma60 <= 25.3947 )
						if( ma60 <= 25.1299 )
							if( ma15 <= 11.7595 )
								if( ma45 <= 11.3659 )
									ret := 0.014639
								if( ma45 > 11.3659 )
									ret := -0.194758
							if( ma15 > 11.7595 )
								if( ma35 <= 12.07 )
									ret := 0.190900
								if( ma35 > 12.07 )
									ret := -0.000212
						if( ma60 > 25.1299 )
							if( ma30 <= 25.1558 )
								if( ma90 <= 25.2331 )
									ret := 0.957746 // buy
								if( ma90 > 25.2331 )
									ret := 0.537634
							if( ma30 > 25.1558 )
								if( ma10_colorInt <= 1.5 )
									ret := -0.116959
								if( ma10_colorInt > 1.5 )
									ret := 0.323077
					if( ma60 > 25.3947 )
						if( ma85 <= 25.5439 )
							if( ma40 <= 25.4465 )
								if( ma25 <= 25.3332 )
									ret := -0.944444 // sell
								if( ma25 > 25.3332 )
									ret := 0.133333
							if( ma40 > 25.4465 )
								if( ma65 <= 25.5198 )
									ret := -0.667870
								if( ma65 > 25.5198 )
									ret := 0.020408
						if( ma85 > 25.5439 )
							if( ma75 <= 25.5977 )
								if( ma65 <= 25.6158 )
									ret := 0.222222
								if( ma65 > 25.6158 )
									ret := 1.000000 // buy
							if( ma75 > 25.5977 )
								ret := 0.000000
				if( ma100 > 25.5702 )
					if( ma40 <= 25.8066 )
						if( ma75 <= 25.7089 )
							if( ma100 <= 25.6158 )
								if( ma05_colorInt <= 2.5 )
									ret := 0.166667
								if( ma05_colorInt > 2.5 )
									ret := 0.660000
							if( ma100 > 25.6158 )
								if( ma20 <= 25.7495 )
									ret := 0.076923
								if( ma20 > 25.7495 )
									ret := 0.875000 // buy
						if( ma75 > 25.7089 )
							if( ma15 <= 25.7792 )
								if( ma10 <= 25.6997 )
									ret := 0.608511
								if( ma10 > 25.6997 )
									ret := -0.368421
							if( ma15 > 25.7792 )
								ret := 1.000000 // buy
					if( ma40 > 25.8066 )
						if( ma30 <= 25.8687 )
							if( ma20 <= 25.7883 )
								if( ma05 <= 25.6716 )
									ret := 0.333333
								if( ma05 > 25.6716 )
									ret := 0.400000
							if( ma20 > 25.7883 )
								if( ma45 <= 25.8326 )
									ret := -0.111111
								if( ma45 > 25.8326 )
									ret := -0.782609 // sell
						if( ma30 > 25.8687 )
							if( ma100 <= 25.7415 )
								if( ma100 <= 25.6774 )
									ret := -0.133333
								if( ma100 > 25.6774 )
									ret := 0.911765 // buy
							if( ma100 > 25.7415 )
								if( ma90 <= 25.8356 )
									ret := -0.195652
								if( ma90 > 25.8356 )
									ret := 1.000000 // buy
			if( ma50 > 25.8875 )
				if( ma25 <= 26.1587 )
					if( ma55_colorInt <= 1.5 )
						if( ma30 <= 25.9658 )
							ret := -0.142857
						if( ma30 > 25.9658 )
							if( ma65 <= 26.0926 )
								if( ma70 <= 25.8773 )
									ret := -0.916667 // sell
								if( ma70 > 25.8773 )
									ret := -0.474747
							if( ma65 > 26.0926 )
								ret := -1.000000 // sell
					if( ma55_colorInt > 1.5 )
						if( ma15_colorInt <= 3.5 )
							if( ma70 <= 26.0713 )
								if( ma20 <= 26.0672 )
									ret := -0.042373
								if( ma20 > 26.0672 )
									ret := -0.962963 // sell
							if( ma70 > 26.0713 )
								if( ma100 <= 26.0522 )
									ret := -0.181818
								if( ma100 > 26.0522 )
									ret := -0.769231 // sell
						if( ma15_colorInt > 3.5 )
							ret := 0.736842 // buy
				if( ma25 > 26.1587 )
					if( ma40 <= 26.7744 )
						if( ma60 <= 26.5947 )
							if( ma20 <= 26.2722 )
								if( ma50 <= 26.2586 )
									ret := -0.172414
								if( ma50 > 26.2586 )
									ret := 0.843137 // buy
							if( ma20 > 26.2722 )
								if( ma85 <= 26.0886 )
									ret := 0.267606
								if( ma85 > 26.0886 )
									ret := -0.150628
						if( ma60 > 26.5947 )
							if( ma75 <= 26.9206 )
								if( ma80 <= 26.6702 )
									ret := 0.789474 // buy
								if( ma80 > 26.6702 )
									ret := 0.358974
							if( ma75 > 26.9206 )
								ret := -0.866667 // sell
					if( ma40 > 26.7744 )
						if( ma90_colorInt <= 2.5 )
							if( ma90 <= 26.6128 )
								if( ma55 <= 26.8071 )
									ret := -0.487179
								if( ma55 > 26.8071 )
									ret := -1.000000 // sell
							if( ma90 > 26.6128 )
								if( ma35 <= 28.0931 )
									ret := -0.031421
								if( ma35 > 28.0931 )
									ret := -0.888889 // sell
						if( ma90_colorInt > 2.5 )
							if( ma30 <= 26.8598 )
								if( ma30_colorInt <= 3.5 )
									ret := 0.500000
								if( ma30_colorInt > 3.5 )
									ret := -0.636364
							if( ma30 > 26.8598 )
								if( ma25 <= 27.184 )
									ret := -0.808383 // sell
								if( ma25 > 27.184 )
									ret := 0.000000
		if( ma50_colorInt > 3.5 )
			if( ma85_colorInt <= 2.5 )
				if( ma90 <= 12.7951 )
					ret := -0.818182 // sell
				if( ma90 > 12.7951 )
					if( ma40 <= 19.9531 )
						if( ma35_colorInt <= 3 )
							ret := -0.600000
						if( ma35_colorInt > 3 )
							if( ma10 <= 13.0544 )
								ret := 0.000000
							if( ma10 > 13.0544 )
								if( ma15 <= 14.3166 )
									ret := 0.891892 // buy
								if( ma15 > 14.3166 )
									ret := 0.536765
					if( ma40 > 19.9531 )
						if( ma50 <= 24.8518 )
							if( ma30 <= 24.1764 )
								if( ma60 <= 24.0772 )
									ret := -0.133333
								if( ma60 > 24.0772 )
									ret := 1.000000 // buy
							if( ma30 > 24.1764 )
								ret := -1.000000 // sell
						if( ma50 > 24.8518 )
							if( ma45 <= 25.7538 )
								ret := 0.666667
							if( ma45 > 25.7538 )
								ret := 0.105263
			if( ma85_colorInt > 2.5 )
				if( ma10 <= 26.7558 )
					if( ma45 <= 13.9636 )
						if( ma85 <= 12.7999 )
							if( ma60 <= 11.4806 )
								if( ma80 <= 11.3396 )
									ret := -0.333333
								if( ma80 > 11.3396 )
									ret := -0.782609 // sell
							if( ma60 > 11.4806 )
								if( ma30_colorInt <= 1.5 )
									ret := -0.593750
								if( ma30_colorInt > 1.5 )
									ret := -0.145299
						if( ma85 > 12.7999 )
							if( ma35 <= 13.0204 )
								if( ma65 <= 12.9789 )
									ret := 0.274336
								if( ma65 > 12.9789 )
									ret := 0.705882 // buy
							if( ma35 > 13.0204 )
								if( ma45_colorInt <= 3.5 )
									ret := 0.595506
								if( ma45_colorInt > 3.5 )
									ret := 0.066510
					if( ma45 > 13.9636 )
						if( ma35 <= 25.5798 )
							if( ma15 <= 21.8232 )
								if( ma65 <= 21.6736 )
									ret := -0.151700
								if( ma65 > 21.6736 )
									ret := -0.633333
							if( ma15 > 21.8232 )
								if( ma65 <= 22.4399 )
									ret := 0.405063
								if( ma65 > 22.4399 )
									ret := -0.063918
						if( ma35 > 25.5798 )
							if( ma90 <= 25.7987 )
								if( ma05 <= 25.8008 )
									ret := -0.560976
								if( ma05 > 25.8008 )
									ret := -0.916667 // sell
							if( ma90 > 25.7987 )
								if( ma75_colorInt <= 3.5 )
									ret := 0.023256
								if( ma75_colorInt > 3.5 )
									ret := -0.379310
				if( ma10 > 26.7558 )
					if( ma25 <= 26.9405 )
						if( ma100 <= 26.7645 )
							ret := 0.600000
						if( ma100 > 26.7645 )
							if( ma35 <= 26.7813 )
								ret := 0.857143 // buy
							if( ma35 > 26.7813 )
								ret := 1.000000 // buy
					if( ma25 > 26.9405 )
						ret := -0.363636
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_RIVN_5Min_48622716(ma05, ma50_colorInt, ma90, ma35_colorInt, ma90_colorInt, ma55_colorInt, ma20, ma15_colorInt, ma40_colorInt, ma45_colorInt, ma65_colorInt, ma75_colorInt, ma35, ma30, ma60, ma75, ma05_colorInt, ma45, ma40, ma30_colorInt, ma25, ma100, ma50, ma70_colorInt, ma10_colorInt, ma20_colorInt, ma60_colorInt, ma25_colorInt, ma10, ma15, ma80, ma65, ma85_colorInt, ma55, ma70, ma85, ma80_colorInt)

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


