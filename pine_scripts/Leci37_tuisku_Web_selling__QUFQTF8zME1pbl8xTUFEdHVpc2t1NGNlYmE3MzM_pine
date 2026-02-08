//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Madrid_Moving_Average_Ribbon
// ID_model: AAPL_30Min_1MAD_4ceba733 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAPL_30Min_1MAD_4ceba733", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAPL_30Min_4ceba733(ma65, ma15_colorInt, ma90_colorInt, ma75, ma10_colorInt, ma100, ma65_colorInt, ma50, ma55_colorInt, ma80_colorInt, ma70, ma20, ma30_colorInt, ma60, ma05, ma25, ma60_colorInt, ma35, ma25_colorInt, ma05_colorInt, ma90, ma80, ma40_colorInt, ma85, ma75_colorInt, ma30, ma40, ma55, ma15, ma35_colorInt, ma70_colorInt, ma45, ma20_colorInt, ma10, ma45_colorInt, ma85_colorInt, ma50_colorInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( ma90 <= 322.776 )
		if( ma20 <= 317.996 )
			if( ma35 <= 144.426 )
				if( ma50 <= 134.584 )
					if( ma70 <= 138.617 )
						if( ma40 <= 134.55 )
							if( ma75 <= 91.4504 )
								if( ma80 <= 91.3085 )
									ret := 0.964286 // buy
								if( ma80 > 91.3085 )
									ret := 0.733333 // buy
							if( ma75 > 91.4504 )
								if( ma15_colorInt <= 3.5 )
									ret := 0.026719
								if( ma15_colorInt > 3.5 )
									ret := -0.075441
						if( ma40 > 134.55 )
							if( ma100 <= 134.609 )
								if( ma05 <= 134.806 )
									ret := 0.000000
								if( ma05 > 134.806 )
									ret := -0.704225 // sell
							if( ma100 > 134.609 )
								ret := -1.000000 // sell
					if( ma70 > 138.617 )
						if( ma75 <= 144.451 )
							ret := -1.000000 // sell
						if( ma75 > 144.451 )
							ret := -0.875000 // sell
				if( ma50 > 134.584 )
					if( ma55 <= 134.939 )
						if( ma85 <= 134.509 )
							if( ma35 <= 135.273 )
								if( ma60 <= 134.56 )
									ret := 0.238095
								if( ma60 > 134.56 )
									ret := -0.315789
							if( ma35 > 135.273 )
								ret := 1.000000 // buy
						if( ma85 > 134.509 )
							if( ma60_colorInt <= 3.5 )
								if( ma20 <= 134.397 )
									ret := 0.555556
								if( ma20 > 134.397 )
									ret := 0.921739 // buy
							if( ma60_colorInt > 3.5 )
								ret := -0.045455
					if( ma55 > 134.939 )
						if( ma45 <= 134.86 )
							if( ma15 <= 133.434 )
								if( ma05 <= 130.268 )
									ret := -1.000000 // sell
								if( ma05 > 130.268 )
									ret := 0.833333 // buy
							if( ma15 > 133.434 )
								if( ma60 <= 135.352 )
									ret := -0.928571 // sell
								if( ma60 > 135.352 )
									ret := -1.000000 // sell
						if( ma45 > 134.86 )
							if( ma15 <= 133.904 )
								if( ma35 <= 133.899 )
									ret := -1.000000 // sell
								if( ma35 > 133.899 )
									ret := 0.762376 // buy
							if( ma15 > 133.904 )
								if( ma25 <= 136.993 )
									ret := -0.046396
								if( ma25 > 136.993 )
									ret := 0.127506
			if( ma35 > 144.426 )
				if( ma05 <= 303.232 )
					if( ma15 <= 299.983 )
						if( ma25 <= 142.43 )
							if( ma05_colorInt <= 3.5 )
								ret := 1.000000 // buy
							if( ma05_colorInt > 3.5 )
								ret := 0.583333
						if( ma25 > 142.43 )
							if( ma75 <= 147.119 )
								if( ma20_colorInt <= 2.5 )
									ret := -0.046190
								if( ma20_colorInt > 2.5 )
									ret := -0.246590
							if( ma75 > 147.119 )
								if( ma55 <= 146.895 )
									ret := 0.523490
								if( ma55 > 146.895 )
									ret := -0.017967
					if( ma15 > 299.983 )
						if( ma35_colorInt <= 2.5 )
							if( ma50 <= 299.163 )
								if( ma45 <= 298.962 )
									ret := -0.684211
								if( ma45 > 298.962 )
									ret := -1.000000 // sell
							if( ma50 > 299.163 )
								ret := 0.090909
						if( ma35_colorInt > 2.5 )
							if( ma15 <= 301.363 )
								if( ma15 <= 300.471 )
									ret := -0.900000 // sell
								if( ma15 > 300.471 )
									ret := -1.000000 // sell
							if( ma15 > 301.363 )
								ret := -0.684211
				if( ma05 > 303.232 )
					if( ma60 <= 313.263 )
						if( ma100 <= 312.761 )
							if( ma85 <= 309.598 )
								if( ma60_colorInt <= 3.5 )
									ret := 0.551331
								if( ma60_colorInt > 3.5 )
									ret := -0.268293
							if( ma85 > 309.598 )
								if( ma30 <= 309.149 )
									ret := -0.923077 // sell
								if( ma30 > 309.149 )
									ret := 0.185430
						if( ma100 > 312.761 )
							if( ma80 <= 313.603 )
								if( ma90_colorInt <= 3.5 )
									ret := 1.000000 // buy
								if( ma90_colorInt > 3.5 )
									ret := 0.352941
							if( ma80 > 313.603 )
								if( ma35_colorInt <= 3.5 )
									ret := 0.705882 // buy
								if( ma35_colorInt > 3.5 )
									ret := 0.000000
					if( ma60 > 313.263 )
						if( ma100 <= 312.583 )
							if( ma35_colorInt <= 1.5 )
								if( ma50 <= 313.477 )
									ret := -0.454545
								if( ma50 > 313.477 )
									ret := -0.962963 // sell
							if( ma35_colorInt > 1.5 )
								if( ma70 <= 313.361 )
									ret := -0.736842 // sell
								if( ma70 > 313.361 )
									ret := 0.000000
						if( ma100 > 312.583 )
							if( ma10 <= 314.143 )
								if( ma30 <= 314.512 )
									ret := 0.000000
								if( ma30 > 314.512 )
									ret := -0.977778 // sell
							if( ma10 > 314.143 )
								if( ma100 <= 321.458 )
									ret := 0.375740
								if( ma100 > 321.458 )
									ret := 1.000000 // buy
		if( ma20 > 317.996 )
			if( ma20 <= 324.446 )
				if( ma05 <= 320.229 )
					if( ma15 <= 319.005 )
						if( ma85 <= 318.694 )
							if( ma25 <= 318.695 )
								if( ma45 <= 317.42 )
									ret := -0.705882 // sell
								if( ma45 > 317.42 )
									ret := -0.323944
							if( ma25 > 318.695 )
								if( ma75 <= 318.785 )
									ret := 0.900000 // buy
								if( ma75 > 318.785 )
									ret := 1.000000 // buy
						if( ma85 > 318.694 )
							if( ma10 <= 316.854 )
								ret := 0.300000
							if( ma10 > 316.854 )
								if( ma60 <= 318.905 )
									ret := 0.000000
								if( ma60 > 318.905 )
									ret := -0.725000 // sell
					if( ma15 > 319.005 )
						if( ma80 <= 318.694 )
							ret := 0.076923
						if( ma80 > 318.694 )
							if( ma70_colorInt <= 2.5 )
								if( ma45 <= 320.557 )
									ret := -0.937063 // sell
								if( ma45 > 320.557 )
									ret := -0.621622
							if( ma70_colorInt > 2.5 )
								ret := 0.055556
				if( ma05 > 320.229 )
					if( ma45_colorInt <= 1.5 )
						if( ma55 <= 322.044 )
							if( ma40 <= 321.303 )
								if( ma35 <= 318.209 )
									ret := 0.733333 // buy
								if( ma35 > 318.209 )
									ret := -0.289017
							if( ma40 > 321.303 )
								if( ma65 <= 321.297 )
									ret := 0.800000 // buy
								if( ma65 > 321.297 )
									ret := -0.172414
						if( ma55 > 322.044 )
							if( ma100 <= 321.546 )
								if( ma10 <= 323.826 )
									ret := -1.000000 // sell
								if( ma10 > 323.826 )
									ret := -0.300000
							if( ma100 > 321.546 )
								if( ma15 <= 323.434 )
									ret := -0.923077 // sell
								if( ma15 > 323.434 )
									ret := 0.200000
					if( ma45_colorInt > 1.5 )
						if( ma55 <= 321.817 )
							if( ma50_colorInt <= 3.5 )
								if( ma25 <= 321.461 )
									ret := 0.953488 // buy
								if( ma25 > 321.461 )
									ret := 0.421053
							if( ma50_colorInt > 3.5 )
								if( ma10 <= 320.528 )
									ret := 0.000000
								if( ma10 > 320.528 )
									ret := 0.350000
						if( ma55 > 321.817 )
							if( ma55 <= 322.85 )
								if( ma45 <= 322.194 )
									ret := -0.923077 // sell
								if( ma45 > 322.194 )
									ret := -0.227273
							if( ma55 > 322.85 )
								ret := 0.727273 // buy
			if( ma20 > 324.446 )
				if( ma25_colorInt <= 1.5 )
					ret := -1.000000 // sell
				if( ma25_colorInt > 1.5 )
					if( ma20 <= 324.602 )
						ret := -0.866667 // sell
					if( ma20 > 324.602 )
						ret := -0.400000
	if( ma90 > 322.776 )
		if( ma85 <= 501.54 )
			if( ma20 <= 462.703 )
				if( ma80 <= 386.726 )
					if( ma45 <= 381.114 )
						if( ma80 <= 341.727 )
							if( ma25 <= 335.701 )
								if( ma40 <= 323.918 )
									ret := 0.750000 // buy
								if( ma40 > 323.918 )
									ret := -0.068293
							if( ma25 > 335.701 )
								if( ma35 <= 344.635 )
									ret := 0.848485 // buy
								if( ma35 > 344.635 )
									ret := 0.200000
						if( ma80 > 341.727 )
							if( ma60 <= 342.368 )
								if( ma100 <= 341.837 )
									ret := -1.000000 // sell
								if( ma100 > 341.837 )
									ret := -0.800000 // sell
							if( ma60 > 342.368 )
								if( ma05 <= 339.753 )
									ret := 1.000000 // buy
								if( ma05 > 339.753 )
									ret := 0.072351
					if( ma45 > 381.114 )
						if( ma20 <= 389.915 )
							if( ma60_colorInt <= 2.5 )
								if( ma60 <= 386.269 )
									ret := 0.631250
								if( ma60 > 386.269 )
									ret := 0.956522 // buy
							if( ma60_colorInt > 2.5 )
								if( ma75 <= 386.063 )
									ret := -0.153846
								if( ma75 > 386.063 )
									ret := 0.463415
						if( ma20 > 389.915 )
							ret := -0.045455
				if( ma80 > 386.726 )
					if( ma15 <= 407.937 )
						if( ma40 <= 389.923 )
							if( ma70 <= 392.016 )
								if( ma55_colorInt <= 2.5 )
									ret := -0.090226
								if( ma55_colorInt > 2.5 )
									ret := -0.636364
							if( ma70 > 392.016 )
								ret := 1.000000 // buy
						if( ma40 > 389.923 )
							if( ma55_colorInt <= 1.5 )
								if( ma25 <= 401.682 )
									ret := -0.969072 // sell
								if( ma25 > 401.682 )
									ret := -0.733333 // sell
							if( ma55_colorInt > 1.5 )
								if( ma25_colorInt <= 2.5 )
									ret := 0.100000
								if( ma25_colorInt > 2.5 )
									ret := -0.500000
					if( ma15 > 407.937 )
						if( ma100 <= 403.558 )
							if( ma05 <= 426.509 )
								if( ma85 <= 394.114 )
									ret := 0.964286 // buy
								if( ma85 > 394.114 )
									ret := 0.583333
							if( ma05 > 426.509 )
								ret := 1.000000 // buy
						if( ma100 > 403.558 )
							if( ma15 <= 459.374 )
								if( ma90 <= 413.194 )
									ret := -0.838710 // sell
								if( ma90 > 413.194 )
									ret := 0.233068
							if( ma15 > 459.374 )
								if( ma85 <= 458.166 )
									ret := -0.800000 // sell
								if( ma85 > 458.166 )
									ret := 0.000000
			if( ma20 > 462.703 )
				if( ma70 <= 483.787 )
					if( ma75 <= 462.374 )
						ret := 0.083333
					if( ma75 > 462.374 )
						if( ma55 <= 470.033 )
							if( ma85 <= 464.75 )
								if( ma25 <= 466.384 )
									ret := 0.692308
								if( ma25 > 466.384 )
									ret := 1.000000 // buy
							if( ma85 > 464.75 )
								ret := 0.076923
						if( ma55 > 470.033 )
							if( ma40 <= 484.744 )
								ret := 1.000000 // buy
							if( ma40 > 484.744 )
								if( ma10 <= 502.008 )
									ret := 0.937500 // buy
								if( ma10 > 502.008 )
									ret := 1.000000 // buy
				if( ma70 > 483.787 )
					if( ma50 <= 503.151 )
						if( ma35 <= 501.435 )
							if( ma60 <= 495.582 )
								ret := -0.428571
							if( ma60 > 495.582 )
								if( ma25 <= 501.544 )
									ret := 0.441176
								if( ma25 > 501.544 )
									ret := 1.000000 // buy
						if( ma35 > 501.435 )
							if( ma15 <= 503.395 )
								ret := -1.000000 // sell
							if( ma15 > 503.395 )
								if( ma50 <= 500.089 )
									ret := -0.800000 // sell
								if( ma50 > 500.089 )
									ret := -0.272727
					if( ma50 > 503.151 )
						ret := 0.863636 // buy
		if( ma85 > 501.54 )
			if( ma05 <= 502.503 )
				if( ma25 <= 501.709 )
					ret := -1.000000 // sell
				if( ma25 > 501.709 )
					if( ma55 <= 503.366 )
						ret := -0.055556
					if( ma55 > 503.366 )
						ret := 0.500000
			if( ma05 > 502.503 )
				if( ma40 <= 502.987 )
					ret := -0.952381 // sell
				if( ma40 > 502.987 )
					ret := -1.000000 // sell
	
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
float op_operation = decision_tree_0_AAPL_30Min_4ceba733(ma65, ma15_colorInt, ma90_colorInt, ma75, ma10_colorInt, ma100, ma65_colorInt, ma50, ma55_colorInt, ma80_colorInt, ma70, ma20, ma30_colorInt, ma60, ma05, ma25, ma60_colorInt, ma35, ma25_colorInt, ma05_colorInt, ma90, ma80, ma40_colorInt, ma85, ma75_colorInt, ma30, ma40, ma55, ma15, ma35_colorInt, ma70_colorInt, ma45, ma20_colorInt, ma10, ma45_colorInt, ma85_colorInt, ma50_colorInt)

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


