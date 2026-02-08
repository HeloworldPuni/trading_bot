//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Madrid_Moving_Average_Ribbon
// ID_model: XRPUSDT_30Min_1MAD_dc90299c Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_XRPUSDT_30Min_1MAD_dc90299c", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_XRPUSDT_30Min_dc90299c(ma25, ma40, ma85, ma05, ma45_colorInt, ma80_colorInt, ma55, ma20, ma65_colorInt, ma05_colorInt, ma10, ma40_colorInt, ma50_colorInt, ma60_colorInt, ma15, ma65, ma85_colorInt, ma45, ma35, ma10_colorInt, ma60, ma100, ma20_colorInt, ma55_colorInt, ma75_colorInt, ma90, ma30, ma15_colorInt, ma25_colorInt, ma80, ma90_colorInt, ma50, ma70_colorInt, ma30_colorInt, ma35_colorInt, ma75, ma70)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( ma75 <= 1.50781 )
		if( ma10_colorInt <= 1.5 )
			if( ma45 <= 1.23644 )
				if( ma20 <= 1.20436 )
					if( ma75 <= 0.530614 )
						if( ma30 <= 0.464403 )
							if( ma05 <= 0.465039 )
								if( ma30_colorInt <= 1.5 )
									ret := -0.049294
								if( ma30_colorInt > 1.5 )
									ret := 0.110429
							if( ma05 > 0.465039 )
								if( ma10 <= 0.476043 )
									ret := -0.595395
								if( ma10 > 0.476043 )
									ret := -0.050000
						if( ma30 > 0.464403 )
							if( ma85 <= 0.46531 )
								if( ma75 <= 0.452769 )
									ret := 0.948718 // buy
								if( ma75 > 0.452769 )
									ret := 0.256039
							if( ma85 > 0.46531 )
								if( ma70 <= 0.470172 )
									ret := -0.296296
								if( ma70 > 0.470172 )
									ret := 0.044937
					if( ma75 > 0.530614 )
						if( ma75 <= 0.550214 )
							if( ma50 <= 0.550303 )
								if( ma50 <= 0.538603 )
									ret := -0.318605
								if( ma50 > 0.538603 )
									ret := 0.031434
							if( ma50 > 0.550303 )
								if( ma15 <= 0.561769 )
									ret := -0.473118
								if( ma15 > 0.561769 )
									ret := -0.850467 // sell
						if( ma75 > 0.550214 )
							if( ma20 <= 1.1643 )
								if( ma05 <= 1.09149 )
									ret := -0.072749
								if( ma05 > 1.09149 )
									ret := 0.149733
							if( ma20 > 1.1643 )
								if( ma05_colorInt <= 1.5 )
									ret := -0.476190
								if( ma05_colorInt > 1.5 )
									ret := 0.250000
				if( ma20 > 1.20436 )
					if( ma25 <= 1.23563 )
						if( ma60 <= 1.18012 )
							if( ma25 <= 1.22205 )
								ret := 1.000000 // buy
							if( ma25 > 1.22205 )
								ret := 0.888889 // buy
						if( ma60 > 1.18012 )
							if( ma85 <= 1.17481 )
								ret := -1.000000 // sell
							if( ma85 > 1.17481 )
								if( ma85 <= 1.18907 )
									ret := 0.920000 // buy
								if( ma85 > 1.18907 )
									ret := 0.566667
					if( ma25 > 1.23563 )
						if( ma20 <= 1.26255 )
							if( ma25 <= 1.24549 )
								ret := -0.133333
							if( ma25 > 1.24549 )
								if( ma65 <= 1.21407 )
									ret := -1.000000 // sell
								if( ma65 > 1.21407 )
									ret := -0.636364
						if( ma20 > 1.26255 )
							if( ma90 <= 1.16968 )
								if( ma20 <= 1.27804 )
									ret := 0.045455
								if( ma20 > 1.27804 )
									ret := 0.666667
							if( ma90 > 1.16968 )
								if( ma85 <= 1.18219 )
									ret := 1.000000 // buy
								if( ma85 > 1.18219 )
									ret := 0.818182 // buy
			if( ma45 > 1.23644 )
				if( ma70 <= 1.37724 )
					if( ma35_colorInt <= 3 )
						if( ma70 <= 1.23151 )
							if( ma75 <= 1.20364 )
								ret := -0.307692
							if( ma75 > 1.20364 )
								if( ma65 <= 1.22552 )
									ret := -0.785714 // sell
								if( ma65 > 1.22552 )
									ret := -0.983333 // sell
						if( ma70 > 1.23151 )
							if( ma40 <= 1.27861 )
								if( ma75 <= 1.27155 )
									ret := -0.225532
								if( ma75 > 1.27155 )
									ret := 1.000000 // buy
							if( ma40 > 1.27861 )
								if( ma05_colorInt <= 1.5 )
									ret := -0.667665
								if( ma05_colorInt > 1.5 )
									ret := 0.160714
					if( ma35_colorInt > 3 )
						if( ma80 <= 1.3185 )
							ret := 0.764706 // buy
						if( ma80 > 1.3185 )
							if( ma25 <= 1.35392 )
								ret := -0.666667
							if( ma25 > 1.35392 )
								if( ma05 <= 1.39641 )
									ret := 0.857143 // buy
								if( ma05 > 1.39641 )
									ret := -0.200000
				if( ma70 > 1.37724 )
					if( ma75_colorInt <= 2.5 )
						if( ma75 <= 1.4424 )
							if( ma35 <= 1.42649 )
								if( ma85 <= 1.38238 )
									ret := 0.981818 // buy
								if( ma85 > 1.38238 )
									ret := 0.913043 // buy
							if( ma35 > 1.42649 )
								if( ma40 <= 1.44641 )
									ret := -0.666667
								if( ma40 > 1.44641 )
									ret := 1.000000 // buy
						if( ma75 > 1.4424 )
							if( ma70 <= 1.49105 )
								if( ma50 <= 1.50027 )
									ret := -0.631579
								if( ma50 > 1.50027 )
									ret := 0.035714
							if( ma70 > 1.49105 )
								if( ma15 <= 1.57077 )
									ret := 0.911765 // buy
								if( ma15 > 1.57077 )
									ret := -0.176471
					if( ma75_colorInt > 2.5 )
						if( ma25 <= 1.4043 )
							ret := 0.363636
						if( ma25 > 1.4043 )
							if( ma10 <= 1.53754 )
								if( ma90 <= 1.4746 )
									ret := -0.581818
								if( ma90 > 1.4746 )
									ret := -1.000000 // sell
							if( ma10 > 1.53754 )
								ret := -0.076923
		if( ma10_colorInt > 1.5 )
			if( ma70 <= 1.34556 )
				if( ma20 <= 0.610007 )
					if( ma75 <= 0.230643 )
						if( ma10 <= 0.223388 )
							if( ma10 <= 0.217399 )
								if( ma15_colorInt <= 3.5 )
									ret := 0.894737 // buy
								if( ma15_colorInt > 3.5 )
									ret := 0.138889
							if( ma10 > 0.217399 )
								if( ma15 <= 0.219404 )
									ret := -0.829787 // sell
								if( ma15 > 0.219404 )
									ret := 0.053191
						if( ma10 > 0.223388 )
							if( ma65 <= 0.229151 )
								if( ma30_colorInt <= 2.5 )
									ret := 1.000000 // buy
								if( ma30_colorInt > 2.5 )
									ret := 0.686275
							if( ma65 > 0.229151 )
								if( ma80 <= 0.230015 )
									ret := -0.169811
								if( ma80 > 0.230015 )
									ret := 0.939394 // buy
					if( ma75 > 0.230643 )
						if( ma65 <= 0.589587 )
							if( ma10_colorInt <= 3.5 )
								if( ma90 <= 0.23368 )
									ret := -0.425197
								if( ma90 > 0.23368 )
									ret := 0.052859
							if( ma10_colorInt > 3.5 )
								if( ma50 <= 0.584828 )
									ret := -0.017163
								if( ma50 > 0.584828 )
									ret := -0.256250
						if( ma65 > 0.589587 )
							if( ma50 <= 0.616199 )
								if( ma80 <= 0.617591 )
									ret := 0.117413
								if( ma80 > 0.617591 )
									ret := 0.666667
							if( ma50 > 0.616199 )
								if( ma30 <= 0.605997 )
									ret := 0.500000
								if( ma30 > 0.605997 )
									ret := -0.490909
				if( ma20 > 0.610007 )
					if( ma20 <= 0.650929 )
						if( ma90_colorInt <= 3.5 )
							if( ma70 <= 0.658252 )
								if( ma100 <= 0.650589 )
									ret := -0.124826
								if( ma100 > 0.650589 )
									ret := 0.225352
							if( ma70 > 0.658252 )
								if( ma85 <= 0.688133 )
									ret := -0.593750
								if( ma85 > 0.688133 )
									ret := 0.722222 // buy
						if( ma90_colorInt > 3.5 )
							if( ma65 <= 0.618211 )
								if( ma25 <= 0.613939 )
									ret := 0.289855
								if( ma25 > 0.613939 )
									ret := -0.094737
							if( ma65 > 0.618211 )
								if( ma15 <= 0.620269 )
									ret := -0.096774
								if( ma15 > 0.620269 )
									ret := 0.370588
					if( ma20 > 0.650929 )
						if( ma45 <= 1.32632 )
							if( ma05_colorInt <= 1.5 )
								if( ma60 <= 0.833899 )
									ret := -0.024691
								if( ma60 > 0.833899 )
									ret := -0.329146
							if( ma05_colorInt > 1.5 )
								if( ma35 <= 1.01821 )
									ret := -0.000561
								if( ma35 > 1.01821 )
									ret := 0.071298
						if( ma45 > 1.32632 )
							if( ma25_colorInt <= 2.5 )
								if( ma40_colorInt <= 1.5 )
									ret := -0.593750
								if( ma40_colorInt > 1.5 )
									ret := 0.277778
							if( ma25_colorInt > 2.5 )
								if( ma20_colorInt <= 3.5 )
									ret := -0.875000 // sell
								if( ma20_colorInt > 3.5 )
									ret := 0.214286
			if( ma70 > 1.34556 )
				if( ma60 <= 1.50381 )
					if( ma20_colorInt <= 3.5 )
						if( ma85 <= 1.34803 )
							if( ma30 <= 1.36421 )
								ret := 0.777778 // buy
							if( ma30 > 1.36421 )
								if( ma100 <= 1.33264 )
									ret := 0.000000
								if( ma100 > 1.33264 )
									ret := -1.000000 // sell
						if( ma85 > 1.34803 )
							if( ma30 <= 1.38453 )
								if( ma25 <= 1.32753 )
									ret := 0.074074
								if( ma25 > 1.32753 )
									ret := 0.665541
							if( ma30 > 1.38453 )
								if( ma30 <= 1.4245 )
									ret := -0.082645
								if( ma30 > 1.4245 )
									ret := 0.385027
					if( ma20_colorInt > 3.5 )
						if( ma05 <= 1.37266 )
							if( ma40 <= 1.35959 )
								if( ma20 <= 1.33269 )
									ret := -0.333333
								if( ma20 > 1.33269 )
									ret := 0.555556
							if( ma40 > 1.35959 )
								if( ma70 <= 1.42197 )
									ret := -0.887097 // sell
								if( ma70 > 1.42197 )
									ret := -0.333333
						if( ma05 > 1.37266 )
							if( ma75 <= 1.46864 )
								if( ma35 <= 1.4059 )
									ret := 0.285714
								if( ma35 > 1.4059 )
									ret := 0.687500
							if( ma75 > 1.46864 )
								if( ma100 <= 1.49247 )
									ret := -0.961538 // sell
								if( ma100 > 1.49247 )
									ret := 0.000000
				if( ma60 > 1.50381 )
					if( ma45 <= 1.52985 )
						if( ma20 <= 1.52951 )
							ret := -0.555556
						if( ma20 > 1.52951 )
							if( ma15 <= 1.5537 )
								ret := -1.000000 // sell
							if( ma15 > 1.5537 )
								ret := -0.923077 // sell
					if( ma45 > 1.52985 )
						ret := 0.555556
	if( ma75 > 1.50781 )
		if( ma45 <= 1.51249 )
			if( ma10 <= 1.47343 )
				if( ma15_colorInt <= 3.5 )
					if( ma100 <= 1.52498 )
						if( ma25 <= 1.47165 )
							ret := -0.300000
						if( ma25 > 1.47165 )
							ret := -1.000000 // sell
					if( ma100 > 1.52498 )
						if( ma20 <= 1.47274 )
							ret := -1.000000 // sell
						if( ma20 > 1.47274 )
							ret := -0.750000 // sell
				if( ma15_colorInt > 3.5 )
					ret := -0.090909
			if( ma10 > 1.47343 )
				ret := -0.272727
		if( ma45 > 1.51249 )
			if( ma25 <= 1.52438 )
				if( ma35 <= 1.52689 )
					if( ma05 <= 1.44773 )
						ret := 0.708333 // buy
					if( ma05 > 1.44773 )
						if( ma20 <= 1.50916 )
							if( ma70 <= 1.53436 )
								ret := -0.333333
							if( ma70 > 1.53436 )
								ret := -1.000000 // sell
						if( ma20 > 1.50916 )
							if( ma75 <= 1.54067 )
								ret := 0.705882 // buy
							if( ma75 > 1.54067 )
								ret := -0.266667
				if( ma35 > 1.52689 )
					if( ma25 <= 1.52344 )
						ret := 0.956522 // buy
					if( ma25 > 1.52344 )
						ret := 0.555556
			if( ma25 > 1.52438 )
				if( ma05 <= 1.58527 )
					if( ma85 <= 1.63478 )
						if( ma80_colorInt <= 2.5 )
							if( ma15_colorInt <= 1.5 )
								if( ma30 <= 1.57843 )
									ret := 0.692308
								if( ma30 > 1.57843 )
									ret := -0.500000
							if( ma15_colorInt > 1.5 )
								if( ma50 <= 1.58309 )
									ret := -0.287879
								if( ma50 > 1.58309 )
									ret := 0.438596
						if( ma80_colorInt > 2.5 )
							if( ma85 <= 1.55893 )
								if( ma05 <= 1.56782 )
									ret := -0.945455 // sell
								if( ma05 > 1.56782 )
									ret := -0.350000
							if( ma85 > 1.55893 )
								if( ma75 <= 1.55844 )
									ret := 0.800000 // buy
								if( ma75 > 1.55844 )
									ret := -0.378641
					if( ma85 > 1.63478 )
						if( ma15 <= 1.60474 )
							if( ma60 <= 1.64731 )
								ret := 0.500000
							if( ma60 > 1.64731 )
								ret := 1.000000 // buy
						if( ma15 > 1.60474 )
							ret := 0.285714
				if( ma05 > 1.58527 )
					if( ma15_colorInt <= 1.5 )
						if( ma60 <= 1.64278 )
							if( ma65 <= 1.53585 )
								ret := -0.428571
							if( ma65 > 1.53585 )
								if( ma05 <= 1.6288 )
									ret := -0.825758 // sell
								if( ma05 > 1.6288 )
									ret := -0.987500 // sell
						if( ma60 > 1.64278 )
							if( ma50 <= 1.75068 )
								if( ma05 <= 1.83549 )
									ret := 0.380952
								if( ma05 > 1.83549 )
									ret := -1.000000 // sell
							if( ma50 > 1.75068 )
								ret := -1.000000 // sell
					if( ma15_colorInt > 1.5 )
						if( ma30 <= 1.63772 )
							if( ma100 <= 1.65938 )
								if( ma05 <= 1.61439 )
									ret := -0.728070 // sell
								if( ma05 > 1.61439 )
									ret := -0.210526
							if( ma100 > 1.65938 )
								if( ma30 <= 1.62594 )
									ret := 0.562500
								if( ma30 > 1.62594 )
									ret := -0.653846
						if( ma30 > 1.63772 )
							if( ma80 <= 1.61183 )
								if( ma100 <= 1.59582 )
									ret := 1.000000 // buy
								if( ma100 > 1.59582 )
									ret := 0.333333
							if( ma80 > 1.61183 )
								if( ma40 <= 1.76027 )
									ret := -0.522523
								if( ma40 > 1.76027 )
									ret := 0.141026
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_XRPUSDT_30Min_dc90299c(ma25, ma40, ma85, ma05, ma45_colorInt, ma80_colorInt, ma55, ma20, ma65_colorInt, ma05_colorInt, ma10, ma40_colorInt, ma50_colorInt, ma60_colorInt, ma15, ma65, ma85_colorInt, ma45, ma35, ma10_colorInt, ma60, ma100, ma20_colorInt, ma55_colorInt, ma75_colorInt, ma90, ma30, ma15_colorInt, ma25_colorInt, ma80, ma90_colorInt, ma50, ma70_colorInt, ma30_colorInt, ma35_colorInt, ma75, ma70)

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


