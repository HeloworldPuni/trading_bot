//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Madrid_Moving_Average_Ribbon
// ID_model: MSFT_1Min_1MAD_cbed85cd Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_MSFT_1Min_1MAD_cbed85cd", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_MSFT_1Min_cbed85cd(ma15, ma70_colorInt, ma75_colorInt, ma70, ma40_colorInt, ma80_colorInt, ma20, ma20_colorInt, ma60, ma50, ma65_colorInt, ma45, ma55, ma05_colorInt, ma35_colorInt, ma10_colorInt, ma30, ma25_colorInt, ma100, ma65, ma85, ma80, ma60_colorInt, ma85_colorInt, ma90, ma90_colorInt, ma25, ma40, ma50_colorInt, ma35, ma30_colorInt, ma45_colorInt, ma05, ma75, ma55_colorInt, ma10, ma15_colorInt)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( ma65_colorInt <= 1.5 )
		if( ma45 <= 404.459 )
			if( ma25_colorInt <= 3.5 )
				if( ma85 <= 397.015 )
					if( ma35 <= 396.965 )
						if( ma25 <= 396.849 )
							if( ma100 <= 394.596 )
								if( ma75 <= 394.084 )
									ret := 0.204263
								if( ma75 > 394.084 )
									ret := -0.340000
							if( ma100 > 394.596 )
								if( ma85 <= 395.839 )
									ret := 0.651685
								if( ma85 > 395.839 )
									ret := 0.071429
						if( ma25 > 396.849 )
							if( ma75_colorInt <= 2 )
								if( ma15 <= 397.522 )
									ret := -0.183333
								if( ma15 > 397.522 )
									ret := -0.852941 // sell
							if( ma75_colorInt > 2 )
								ret := -1.000000 // sell
					if( ma35 > 396.965 )
						if( ma60 <= 397.332 )
							if( ma25 <= 397.226 )
								ret := 0.090909
							if( ma25 > 397.226 )
								if( ma35 <= 397.739 )
									ret := 0.891304 // buy
								if( ma35 > 397.739 )
									ret := 0.518519
						if( ma60 > 397.332 )
							if( ma60 <= 397.62 )
								if( ma25 <= 398.612 )
									ret := -0.615385
								if( ma25 > 398.612 )
									ret := 0.500000
							if( ma60 > 397.62 )
								ret := 1.000000 // buy
				if( ma85 > 397.015 )
					if( ma70 <= 398.099 )
						if( ma90 <= 397.333 )
							if( ma20 <= 398.165 )
								if( ma20 <= 397.676 )
									ret := 0.181818
								if( ma20 > 397.676 )
									ret := 0.736842 // buy
							if( ma20 > 398.165 )
								if( ma60 <= 397.991 )
									ret := -0.733333 // sell
								if( ma60 > 397.991 )
									ret := -0.259259
						if( ma90 > 397.333 )
							if( ma25 <= 398.567 )
								if( ma55 <= 397.873 )
									ret := 0.450000
								if( ma55 > 397.873 )
									ret := -0.032258
							if( ma25 > 398.567 )
								if( ma20 <= 399.72 )
									ret := -0.679012
								if( ma20 > 399.72 )
									ret := 1.000000 // buy
					if( ma70 > 398.099 )
						if( ma50 <= 399.788 )
							if( ma05 <= 400.103 )
								if( ma25 <= 399.192 )
									ret := 0.176678
								if( ma25 > 399.192 )
									ret := 0.699571
							if( ma05 > 400.103 )
								if( ma30 <= 399.871 )
									ret := -0.316327
								if( ma30 > 399.871 )
									ret := 0.453488
						if( ma50 > 399.788 )
							if( ma80 <= 400.336 )
								if( ma10_colorInt <= 1.5 )
									ret := -0.552288
								if( ma10_colorInt > 1.5 )
									ret := 0.014815
							if( ma80 > 400.336 )
								if( ma25 <= 404.891 )
									ret := 0.208820
								if( ma25 > 404.891 )
									ret := -0.537634
			if( ma25_colorInt > 3.5 )
				if( ma65 <= 398.13 )
					ret := 0.230769
				if( ma65 > 398.13 )
					if( ma80 <= 401.505 )
						ret := -1.000000 // sell
					if( ma80 > 401.505 )
						ret := -0.714286 // sell
		if( ma45 > 404.459 )
			if( ma80 <= 407.88 )
				if( ma70 <= 407.486 )
					if( ma30 <= 407.202 )
						if( ma90 <= 407.031 )
							if( ma20 <= 407.465 )
								if( ma80 <= 403.865 )
									ret := 0.571429
								if( ma80 > 403.865 )
									ret := -0.132647
							if( ma20 > 407.465 )
								if( ma80 <= 404.324 )
									ret := -1.000000 // sell
								if( ma80 > 404.324 )
									ret := -0.900000 // sell
						if( ma90 > 407.031 )
							if( ma25 <= 407.127 )
								ret := -0.818182 // sell
							if( ma25 > 407.127 )
								ret := -1.000000 // sell
					if( ma30 > 407.202 )
						if( ma55 <= 407.344 )
							if( ma10_colorInt <= 1.5 )
								if( ma45 <= 407.054 )
									ret := -0.294118
								if( ma45 > 407.054 )
									ret := 0.572816
							if( ma10_colorInt > 1.5 )
								if( ma75 <= 406.86 )
									ret := -0.840000 // sell
								if( ma75 > 406.86 )
									ret := 0.129630
						if( ma55 > 407.344 )
							if( ma10_colorInt <= 1.5 )
								if( ma20 <= 407.739 )
									ret := -0.018868
								if( ma20 > 407.739 )
									ret := -0.678161
							if( ma10_colorInt > 1.5 )
								if( ma15 <= 407.622 )
									ret := -0.500000
								if( ma15 > 407.622 )
									ret := 0.200000
				if( ma70 > 407.486 )
					if( ma25 <= 408.898 )
						if( ma15 <= 408.516 )
							if( ma90 <= 407.766 )
								if( ma15 <= 408.29 )
									ret := -0.410256
								if( ma15 > 408.29 )
									ret := -0.692308
							if( ma90 > 407.766 )
								if( ma30 <= 408.257 )
									ret := 0.500000
								if( ma30 > 408.257 )
									ret := -0.500000
						if( ma15 > 408.516 )
							if( ma05 <= 409.09 )
								if( ma65 <= 407.78 )
									ret := 0.714286 // buy
								if( ma65 > 407.78 )
									ret := 0.125000
							if( ma05 > 409.09 )
								if( ma10 <= 409.084 )
									ret := -0.571429
								if( ma10 > 409.084 )
									ret := 0.066667
					if( ma25 > 408.898 )
						if( ma05 <= 410.266 )
							if( ma50 <= 408.312 )
								ret := -0.888889 // sell
							if( ma50 > 408.312 )
								ret := -1.000000 // sell
						if( ma05 > 410.266 )
							if( ma20 <= 413.232 )
								ret := -0.083333
							if( ma20 > 413.232 )
								ret := -1.000000 // sell
			if( ma80 > 407.88 )
				if( ma05 <= 408.396 )
					if( ma35 <= 408.055 )
						ret := 0.592593
					if( ma35 > 408.055 )
						if( ma60 <= 408.255 )
							ret := 1.000000 // buy
						if( ma60 > 408.255 )
							if( ma10 <= 408.366 )
								ret := 0.846154 // buy
							if( ma10 > 408.366 )
								ret := 0.500000
				if( ma05 > 408.396 )
					if( ma50 <= 467.403 )
						if( ma40_colorInt <= 2.5 )
							if( ma90 <= 467.356 )
								if( ma10 <= 408.528 )
									ret := -0.574468
								if( ma10 > 408.528 )
									ret := -0.060966
							if( ma90 > 467.356 )
								ret := 1.000000 // buy
						if( ma40_colorInt > 2.5 )
							if( ma50 <= 413.302 )
								ret := -0.545455
							if( ma50 > 413.302 )
								if( ma45_colorInt <= 1.5 )
									ret := -0.061538
								if( ma45_colorInt > 1.5 )
									ret := 0.280702
					if( ma50 > 467.403 )
						if( ma35_colorInt <= 1.5 )
							if( ma35 <= 468.216 )
								if( ma35 <= 467.645 )
									ret := -0.967742 // sell
								if( ma35 > 467.645 )
									ret := -0.138889
							if( ma35 > 468.216 )
								ret := -1.000000 // sell
						if( ma35_colorInt > 1.5 )
							ret := -0.066667
	if( ma65_colorInt > 1.5 )
		if( ma20_colorInt <= 3.5 )
			if( ma15 <= 392.183 )
				if( ma90_colorInt <= 2.5 )
					ret := 1.000000 // buy
				if( ma90_colorInt > 2.5 )
					if( ma35 <= 387.053 )
						ret := 1.000000 // buy
					if( ma35 > 387.053 )
						if( ma25 <= 388.697 )
							if( ma85 <= 389.565 )
								ret := -0.800000 // sell
							if( ma85 > 389.565 )
								ret := -1.000000 // sell
						if( ma25 > 388.697 )
							if( ma100 <= 397.991 )
								if( ma40 <= 392.304 )
									ret := 0.201465
								if( ma40 > 392.304 )
									ret := 0.928571 // buy
							if( ma100 > 397.991 )
								ret := -1.000000 // sell
			if( ma15 > 392.183 )
				if( ma15 <= 393.272 )
					if( ma45 <= 395.268 )
						if( ma70 <= 392.976 )
							if( ma05 <= 391.949 )
								ret := 0.714286 // buy
							if( ma05 > 391.949 )
								if( ma25_colorInt <= 1.5 )
									ret := 0.107143
								if( ma25_colorInt > 1.5 )
									ret := -0.740741 // sell
						if( ma70 > 392.976 )
							if( ma30 <= 393.434 )
								ret := -1.000000 // sell
							if( ma30 > 393.434 )
								ret := -0.909091 // sell
					if( ma45 > 395.268 )
						ret := 0.692308
				if( ma15 > 393.272 )
					if( ma45_colorInt <= 3.5 )
						if( ma65 <= 461.028 )
							if( ma50 <= 460.182 )
								if( ma80 <= 393.747 )
									ret := 0.800000 // buy
								if( ma80 > 393.747 )
									ret := 0.058655
							if( ma50 > 460.182 )
								if( ma100 <= 460.792 )
									ret := 0.741379 // buy
								if( ma100 > 460.792 )
									ret := 0.345238
						if( ma65 > 461.028 )
							if( ma55 <= 464.761 )
								if( ma50 <= 463.393 )
									ret := -0.460751
								if( ma50 > 463.393 )
									ret := -0.076389
							if( ma55 > 464.761 )
								if( ma05 <= 463.841 )
									ret := 1.000000 // buy
								if( ma05 > 463.841 )
									ret := 0.098390
					if( ma45_colorInt > 3.5 )
						if( ma65 <= 412.446 )
							if( ma85_colorInt <= 3.5 )
								if( ma55 <= 399.129 )
									ret := -0.542857
								if( ma55 > 399.129 )
									ret := -0.147541
							if( ma85_colorInt > 3.5 )
								if( ma30 <= 395.752 )
									ret := 0.942857 // buy
								if( ma30 > 395.752 )
									ret := 0.195122
						if( ma65 > 412.446 )
							if( ma50 <= 447.005 )
								if( ma40 <= 412.719 )
									ret := -0.863014 // sell
								if( ma40 > 412.719 )
									ret := -0.152517
							if( ma50 > 447.005 )
								if( ma25 <= 450.141 )
									ret := 0.672414
								if( ma25 > 450.141 )
									ret := -0.015326
		if( ma20_colorInt > 3.5 )
			if( ma15 <= 428.567 )
				if( ma65 <= 428.113 )
					if( ma80 <= 387.814 )
						if( ma65_colorInt <= 3.5 )
							ret := 1.000000 // buy
						if( ma65_colorInt > 3.5 )
							ret := 0.666667
					if( ma80 > 387.814 )
						if( ma10 <= 407.821 )
							if( ma85 <= 399.067 )
								if( ma50 <= 398.389 )
									ret := 0.020022
								if( ma50 > 398.389 )
									ret := 0.941860 // buy
							if( ma85 > 399.067 )
								if( ma80 <= 407.881 )
									ret := -0.135166
								if( ma80 > 407.881 )
									ret := -0.562500
						if( ma10 > 407.821 )
							if( ma70 <= 427.474 )
								if( ma55_colorInt <= 2.5 )
									ret := -0.248996
								if( ma55_colorInt > 2.5 )
									ret := 0.029602
							if( ma70 > 427.474 )
								if( ma50 <= 427.724 )
									ret := -0.683333
								if( ma50 > 427.724 )
									ret := -0.387097
				if( ma65 > 428.113 )
					if( ma65 <= 428.413 )
						if( ma10 <= 427.144 )
							ret := 1.000000 // buy
						if( ma10 > 427.144 )
							if( ma25 <= 427.929 )
								if( ma45 <= 427.872 )
									ret := 0.763158 // buy
								if( ma45 > 427.872 )
									ret := -0.600000
							if( ma25 > 427.929 )
								if( ma90 <= 428.556 )
									ret := 0.944444 // buy
								if( ma90 > 428.556 )
									ret := 0.769231 // buy
					if( ma65 > 428.413 )
						if( ma90 <= 429.841 )
							if( ma55 <= 428.361 )
								if( ma35_colorInt <= 3.5 )
									ret := 0.200000
								if( ma35_colorInt > 3.5 )
									ret := -0.823529 // sell
							if( ma55 > 428.361 )
								if( ma70 <= 428.479 )
									ret := 0.772727 // buy
								if( ma70 > 428.479 )
									ret := 0.063291
						if( ma90 > 429.841 )
							ret := 1.000000 // buy
			if( ma15 > 428.567 )
				if( ma20 <= 451.873 )
					if( ma60 <= 449.219 )
						if( ma85 <= 448.893 )
							if( ma90 <= 448.411 )
								if( ma85 <= 444.926 )
									ret := -0.205155
								if( ma85 > 444.926 )
									ret := 0.099010
							if( ma90 > 448.411 )
								if( ma40_colorInt <= 3.5 )
									ret := -0.521739
								if( ma40_colorInt > 3.5 )
									ret := -0.607843
						if( ma85 > 448.893 )
							if( ma50_colorInt <= 3.5 )
								if( ma40 <= 448.624 )
									ret := 0.555556
								if( ma40 > 448.624 )
									ret := -0.256410
							if( ma50_colorInt > 3.5 )
								if( ma100 <= 449.629 )
									ret := 1.000000 // buy
								if( ma100 > 449.629 )
									ret := 0.800000 // buy
					if( ma60 > 449.219 )
						if( ma75 <= 449.553 )
							if( ma80 <= 449.343 )
								ret := -0.111111
							if( ma80 > 449.343 )
								if( ma55 <= 449.21 )
									ret := -1.000000 // sell
								if( ma55 > 449.21 )
									ret := -0.900000 // sell
						if( ma75 > 449.553 )
							if( ma75 <= 449.747 )
								if( ma100 <= 449.836 )
									ret := -0.115385
								if( ma100 > 449.836 )
									ret := 0.238095
							if( ma75 > 449.747 )
								if( ma20 <= 448.904 )
									ret := 0.071429
								if( ma20 > 448.904 )
									ret := -0.512195
				if( ma20 > 451.873 )
					if( ma25 <= 460.749 )
						if( ma05_colorInt <= 2.5 )
							if( ma70 <= 453.75 )
								if( ma70 <= 452.607 )
									ret := 0.882353 // buy
								if( ma70 > 452.607 )
									ret := 0.000000
							if( ma70 > 453.75 )
								if( ma15_colorInt <= 3.5 )
									ret := -0.461538
								if( ma15_colorInt > 3.5 )
									ret := 0.774194 // buy
						if( ma05_colorInt > 2.5 )
							if( ma100 <= 454.519 )
								if( ma100 <= 453.839 )
									ret := 0.031546
								if( ma100 > 453.839 )
									ret := 0.547945
							if( ma100 > 454.519 )
								if( ma20 <= 455.287 )
									ret := -0.652482
								if( ma20 > 455.287 )
									ret := 0.317919
					if( ma25 > 460.749 )
						if( ma70 <= 465.149 )
							if( ma35 <= 462.108 )
								ret := -0.850000 // sell
							if( ma35 > 462.108 )
								if( ma100 <= 464.502 )
									ret := 0.166667
								if( ma100 > 464.502 )
									ret := -0.708333 // sell
						if( ma70 > 465.149 )
							if( ma55 <= 465.81 )
								if( ma40 <= 465.354 )
									ret := 0.413793
								if( ma40 > 465.354 )
									ret := -0.039216
							if( ma55 > 465.81 )
								if( ma30 <= 467.181 )
									ret := -0.625000
								if( ma30 > 467.181 )
									ret := -0.285714
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_MSFT_1Min_cbed85cd(ma15, ma70_colorInt, ma75_colorInt, ma70, ma40_colorInt, ma80_colorInt, ma20, ma20_colorInt, ma60, ma50, ma65_colorInt, ma45, ma55, ma05_colorInt, ma35_colorInt, ma10_colorInt, ma30, ma25_colorInt, ma100, ma65, ma85, ma80, ma60_colorInt, ma85_colorInt, ma90, ma90_colorInt, ma25, ma40, ma50_colorInt, ma35, ma30_colorInt, ma45_colorInt, ma05, ma75, ma55_colorInt, ma10, ma15_colorInt)

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


