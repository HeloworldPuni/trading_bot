//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: SNAP_15Min_1T00_162559f4 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_15Min_1T00_162559f4", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_15Min_162559f4(ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( ema12 <= 0.004746 )
		if( ema1 <= 49.8548 )
			if( ema1 <= 48.4594 )
				if( ema2 <= 5.42011 )
					if( ema2 <= 5.11975 )
						if( ema3 <= 4.97455 )
							ret := 1.000000 // buy
						if( ema3 > 4.97455 )
							if( ema13 <= -0.06532 )
								if( ema13 <= -0.07652 )
									ret := -0.375000
								if( ema13 > -0.07652 )
									ret := 0.647059
							if( ema13 > -0.06532 )
								if( ema2 <= 5.09178 )
									ret := -1.000000 // sell
								if( ema2 > 5.09178 )
									ret := -0.289474
					if( ema2 > 5.11975 )
						if( ema12 <= -0.006673 )
							if( ema13 <= -0.016834 )
								if( ema2 <= 5.25298 )
									ret := 0.954023 // buy
								if( ema2 > 5.25298 )
									ret := 0.750000 // buy
							if( ema13 > -0.016834 )
								ret := -0.500000
						if( ema12 > -0.006673 )
							ret := -0.750000 // sell
				if( ema2 > 5.42011 )
					if( ema1 <= 5.89418 )
						if( ema1 <= 5.8433 )
							if( ema3 <= 5.90674 )
								if( ema2 <= 5.75569 )
									ret := 0.092555
								if( ema2 > 5.75569 )
									ret := -0.378906
							if( ema3 > 5.90674 )
								ret := 1.000000 // buy
						if( ema1 > 5.8433 )
							if( ema3 <= 5.93475 )
								ret := -1.000000 // sell
							if( ema3 > 5.93475 )
								ret := -0.894737 // sell
					if( ema1 > 5.89418 )
						if( ema3 <= 5.97855 )
							if( ema2 <= 5.92519 )
								ret := 1.000000 // buy
							if( ema2 > 5.92519 )
								if( ema12 <= -0.013188 )
									ret := 0.888889 // buy
								if( ema12 > -0.013188 )
									ret := 0.509434
						if( ema3 > 5.97855 )
							if( ema3 <= 10.0907 )
								if( ema3 <= 6.20153 )
									ret := -0.218837
								if( ema3 > 6.20153 )
									ret := 0.101229
							if( ema3 > 10.0907 )
								if( tema <= 10.419 )
									ret := -0.047852
								if( tema > 10.419 )
									ret := 0.044416
			if( ema1 > 48.4594 )
				if( ema13 <= -0.393646 )
					if( ema13 <= -0.643827 )
						if( ema2 <= 49.8065 )
							if( ema2 <= 49.5085 )
								if( ema1 <= 48.6498 )
									ret := 0.769231 // buy
								if( ema1 > 48.6498 )
									ret := 0.347826
							if( ema2 > 49.5085 )
								if( tema <= 48.5997 )
									ret := 1.000000 // buy
								if( tema > 48.5997 )
									ret := 0.769231 // buy
						if( ema2 > 49.8065 )
							if( tema <= 48.6308 )
								if( ema13 <= -1.16015 )
									ret := -0.700000 // sell
								if( ema13 > -1.16015 )
									ret := -1.000000 // sell
							if( tema > 48.6308 )
								if( ema12 <= -0.605782 )
									ret := 0.800000 // buy
								if( ema12 > -0.605782 )
									ret := 0.266667
					if( ema13 > -0.643827 )
						if( ema13 <= -0.421987 )
							if( ema12 <= -0.165789 )
								if( ema1 <= 49.3136 )
									ret := -0.500000
								if( ema1 > 49.3136 )
									ret := -0.047619
							if( ema12 > -0.165789 )
								ret := -0.857143 // sell
						if( ema13 > -0.421987 )
							if( ema13 <= -0.41105 )
								ret := 0.600000
							if( ema13 > -0.41105 )
								ret := -0.153846
				if( ema13 > -0.393646 )
					if( ema12 <= 0.000806 )
						if( ema12 <= -0.13746 )
							if( ema3 <= 49.0367 )
								ret := 0.333333
							if( ema3 > 49.0367 )
								if( ema3 <= 49.9979 )
									ret := 0.800000 // buy
								if( ema3 > 49.9979 )
									ret := 1.000000 // buy
						if( ema12 > -0.13746 )
							if( tema <= 49.128 )
								if( ema1 <= 48.8375 )
									ret := 0.565789
								if( ema1 > 48.8375 )
									ret := -0.135802
							if( tema > 49.128 )
								if( tema <= 49.4791 )
									ret := 0.678161
								if( tema > 49.4791 )
									ret := 0.420000
					if( ema12 > 0.000806 )
						ret := -0.666667
		if( ema1 > 49.8548 )
			if( ema13 <= -1.92172 )
				if( ema1 <= 69.7127 )
					if( ema13 <= -2.15327 )
						if( tema <= 56.4167 )
							if( ema1 <= 54.4855 )
								ret := 0.923077 // buy
							if( ema1 > 54.4855 )
								ret := 0.833333 // buy
						if( tema > 56.4167 )
							ret := 1.000000 // buy
					if( ema13 > -2.15327 )
						ret := 0.666667
				if( ema1 > 69.7127 )
					ret := 0.529412
			if( ema13 > -1.92172 )
				if( tema <= 49.8642 )
					if( ema2 <= 50.0726 )
						if( ema12 <= -0.122657 )
							ret := -1.000000 // sell
						if( ema12 > -0.122657 )
							ret := -0.272727
					if( ema2 > 50.0726 )
						if( ema1 <= 49.9218 )
							ret := 0.000000
						if( ema1 > 49.9218 )
							if( ema1 <= 49.9807 )
								ret := -0.842105 // sell
							if( ema1 > 49.9807 )
								if( tema <= 49.6339 )
									ret := -0.153846
								if( tema > 49.6339 )
									ret := -0.600000
				if( tema > 49.8642 )
					if( tema <= 76.8535 )
						if( tema <= 55.0115 )
							if( ema1 <= 50.0838 )
								if( ema3 <= 50.0071 )
									ret := 1.000000 // buy
								if( ema3 > 50.0071 )
									ret := 0.681818
							if( ema1 > 50.0838 )
								if( ema1 <= 50.4731 )
									ret := -0.683168
								if( ema1 > 50.4731 )
									ret := -0.110794
						if( tema > 55.0115 )
							if( ema1 <= 62.905 )
								if( ema2 <= 62.7708 )
									ret := 0.070703
								if( ema2 > 62.7708 )
									ret := 0.448133
							if( ema1 > 62.905 )
								if( tema <= 67.1237 )
									ret := -0.286735
								if( tema > 67.1237 )
									ret := 0.051434
					if( tema > 76.8535 )
						if( ema3 <= 79.0804 )
							if( tema <= 78.3228 )
								if( ema13 <= -0.490531 )
									ret := -1.000000 // sell
								if( ema13 > -0.490531 )
									ret := -0.345238
							if( tema > 78.3228 )
								if( ema12 <= -0.169692 )
									ret := 1.000000 // buy
								if( ema12 > -0.169692 )
									ret := -0.166667
						if( ema3 > 79.0804 )
							if( ema1 <= 78.9162 )
								if( tema <= 78.6872 )
									ret := -0.571429
								if( tema > 78.6872 )
									ret := -0.937500 // sell
							if( ema1 > 78.9162 )
								if( ema3 <= 82.7584 )
									ret := -0.306452
								if( ema3 > 82.7584 )
									ret := -0.681818
	if( ema12 > 0.004746 )
		if( tema <= 42.4719 )
			if( ema2 <= 11.4905 )
				if( ema3 <= 9.36021 )
					if( ema13 <= 0.227057 )
						if( ema1 <= 6.36505 )
							if( ema2 <= 6.25255 )
								if( ema12 <= 0.006598 )
									ret := -0.405660
								if( ema12 > 0.006598 )
									ret := 0.005329
							if( ema2 > 6.25255 )
								if( ema3 <= 6.29777 )
									ret := 0.800000 // buy
								if( ema3 > 6.29777 )
									ret := 0.103448
						if( ema1 > 6.36505 )
							if( tema <= 9.39151 )
								if( ema2 <= 7.18108 )
									ret := -0.235256
								if( ema2 > 7.18108 )
									ret := -0.096422
							if( tema > 9.39151 )
								if( ema1 <= 9.46604 )
									ret := -0.660000
								if( ema1 > 9.46604 )
									ret := 0.750000 // buy
					if( ema13 > 0.227057 )
						if( ema3 <= 9.07803 )
							if( tema <= 8.53872 )
								if( ema3 <= 7.7725 )
									ret := 0.862069 // buy
								if( ema3 > 7.7725 )
									ret := -0.739130 // sell
							if( tema > 8.53872 )
								if( ema2 <= 7.69979 )
									ret := -0.076923
								if( ema2 > 7.69979 )
									ret := 0.742857 // buy
						if( ema3 > 9.07803 )
							if( ema2 <= 9.38058 )
								if( ema1 <= 9.44529 )
									ret := -1.000000 // sell
								if( ema1 > 9.44529 )
									ret := -0.400000
							if( ema2 > 9.38058 )
								ret := 0.444444
				if( ema3 > 9.36021 )
					if( tema <= 9.64741 )
						if( tema <= 9.51151 )
							if( ema1 <= 9.39496 )
								if( ema1 <= 9.38867 )
									ret := 0.321429
								if( ema1 > 9.38867 )
									ret := 0.947368 // buy
							if( ema1 > 9.39496 )
								if( tema <= 9.41053 )
									ret := -0.717391 // sell
								if( tema > 9.41053 )
									ret := 0.045070
						if( tema > 9.51151 )
							if( ema12 <= 0.011178 )
								if( tema <= 9.63888 )
									ret := -0.346667
								if( tema > 9.63888 )
									ret := 0.666667
							if( ema12 > 0.011178 )
								if( ema1 <= 9.59053 )
									ret := 0.525672
								if( ema1 > 9.59053 )
									ret := 0.142857
					if( tema > 9.64741 )
						if( ema2 <= 11.4513 )
							if( ema1 <= 9.78336 )
								if( ema3 <= 9.44936 )
									ret := -0.604167
								if( ema3 > 9.44936 )
									ret := -0.174058
							if( ema1 > 9.78336 )
								if( ema3 <= 10.7222 )
									ret := 0.061789
								if( ema3 > 10.7222 )
									ret := -0.058155
						if( ema2 > 11.4513 )
							if( ema13 <= 0.067013 )
								if( ema1 <= 11.4847 )
									ret := 0.682540
								if( ema1 > 11.4847 )
									ret := 0.149425
							if( ema13 > 0.067013 )
								if( ema12 <= 0.036808 )
									ret := 0.866667 // buy
								if( ema12 > 0.036808 )
									ret := -0.024590
			if( ema2 > 11.4905 )
				if( ema3 <= 12.1907 )
					if( ema13 <= 0.497415 )
						if( ema2 <= 11.5479 )
							if( ema3 <= 11.5239 )
								if( tema <= 11.5297 )
									ret := 0.200000
								if( tema > 11.5297 )
									ret := -0.547718
							if( ema3 > 11.5239 )
								ret := 0.181818
						if( ema2 > 11.5479 )
							if( ema2 <= 11.8682 )
								if( ema1 <= 11.9018 )
									ret := -0.096085
								if( ema1 > 11.9018 )
									ret := 0.564706
							if( ema2 > 11.8682 )
								if( ema1 <= 12.3933 )
									ret := -0.298415
								if( ema1 > 12.3933 )
									ret := 0.925926 // buy
					if( ema13 > 0.497415 )
						ret := -1.000000 // sell
				if( ema3 > 12.1907 )
					if( ema1 <= 14.7974 )
						if( ema2 <= 14.6614 )
							if( ema2 <= 14.6264 )
								if( ema3 <= 12.1999 )
									ret := 0.825000 // buy
								if( ema3 > 12.1999 )
									ret := -0.024244
							if( ema2 > 14.6264 )
								if( ema13 <= 0.123101 )
									ret := -0.414414
								if( ema13 > 0.123101 )
									ret := 0.232558
						if( ema2 > 14.6614 )
							if( tema <= 14.6883 )
								if( ema1 <= 14.678 )
									ret := 0.772727 // buy
								if( ema1 > 14.678 )
									ret := 1.000000 // buy
							if( tema > 14.6883 )
								if( ema12 <= 0.075073 )
									ret := 0.147793
								if( ema12 > 0.075073 )
									ret := -0.812500 // sell
					if( ema1 > 14.7974 )
						if( ema2 <= 16.3837 )
							if( tema <= 16.1057 )
								if( ema1 <= 15.7057 )
									ret := -0.148040
								if( ema1 > 15.7057 )
									ret := 0.050289
							if( tema > 16.1057 )
								if( tema <= 16.6389 )
									ret := -0.265349
								if( tema > 16.6389 )
									ret := -0.659091
						if( ema2 > 16.3837 )
							if( ema12 <= 0.076277 )
								if( ema3 <= 19.784 )
									ret := -0.079517
								if( ema3 > 19.784 )
									ret := 0.018176
							if( ema12 > 0.076277 )
								if( ema1 <= 16.6095 )
									ret := 0.402174
								if( ema1 > 16.6095 )
									ret := -0.121059
		if( tema > 42.4719 )
			if( ema13 <= 0.505115 )
				if( ema3 <= 63.0842 )
					if( ema3 <= 62.8281 )
						if( tema <= 43.4247 )
							if( ema12 <= 0.226487 )
								if( ema2 <= 42.2659 )
									ret := -0.192308
								if( ema2 > 42.2659 )
									ret := 0.475524
							if( ema12 > 0.226487 )
								ret := -0.923077 // sell
						if( tema > 43.4247 )
							if( ema1 <= 43.7031 )
								if( ema2 <= 43.4317 )
									ret := -0.375000
								if( ema2 > 43.4317 )
									ret := -0.863636 // sell
							if( ema1 > 43.7031 )
								if( ema3 <= 44.9349 )
									ret := 0.299639
								if( ema3 > 44.9349 )
									ret := -0.015275
					if( ema3 > 62.8281 )
						if( tema <= 63.4613 )
							if( ema2 <= 63.1248 )
								if( ema1 <= 63.1142 )
									ret := 0.339286
								if( ema1 > 63.1142 )
									ret := 0.833333 // buy
							if( ema2 > 63.1248 )
								ret := -0.416667
						if( tema > 63.4613 )
							if( ema1 <= 63.4296 )
								if( ema2 <= 63.1156 )
									ret := 0.583333
								if( ema2 > 63.1156 )
									ret := 0.933333 // buy
							if( ema1 > 63.4296 )
								ret := 0.437500
				if( ema3 > 63.0842 )
					if( ema2 <= 65 )
						if( tema <= 65.1367 )
							if( tema <= 63.4519 )
								if( tema <= 63.3623 )
									ret := -0.625000
								if( tema > 63.3623 )
									ret := -0.958333 // sell
							if( tema > 63.4519 )
								if( ema13 <= 0.43396 )
									ret := -0.317003
								if( ema13 > 0.43396 )
									ret := 0.333333
						if( tema > 65.1367 )
							if( ema2 <= 64.8524 )
								ret := -0.888889 // sell
							if( ema2 > 64.8524 )
								ret := -1.000000 // sell
					if( ema2 > 65 )
						if( ema3 <= 65.4659 )
							if( ema12 <= 0.151627 )
								if( tema <= 65.4593 )
									ret := 0.411765
								if( tema > 65.4593 )
									ret := 0.950000 // buy
							if( ema12 > 0.151627 )
								if( ema3 <= 65.3102 )
									ret := 0.000000
								if( ema3 > 65.3102 )
									ret := 0.466667
						if( ema3 > 65.4659 )
							if( ema3 <= 69.8751 )
								if( tema <= 69.5728 )
									ret := -0.239362
								if( tema > 69.5728 )
									ret := -1.000000 // sell
							if( ema3 > 69.8751 )
								if( ema3 <= 74.9294 )
									ret := 0.117073
								if( ema3 > 74.9294 )
									ret := -0.204942
			if( ema13 > 0.505115 )
				if( ema3 <= 49.0105 )
					if( ema2 <= 48.5943 )
						if( ema2 <= 48.3166 )
							if( ema13 <= 1.13994 )
								if( ema12 <= 0.2503 )
									ret := -0.200000
								if( ema12 > 0.2503 )
									ret := 0.615764
							if( ema13 > 1.13994 )
								if( ema1 <= 42.9695 )
									ret := 0.153846
								if( ema1 > 42.9695 )
									ret := -0.777778 // sell
						if( ema2 > 48.3166 )
							ret := -0.833333 // sell
					if( ema2 > 48.5943 )
						if( ema1 <= 49.1831 )
							ret := 0.666667
						if( ema1 > 49.1831 )
							if( tema <= 50.3173 )
								ret := 1.000000 // buy
							if( tema > 50.3173 )
								ret := 0.761905 // buy
				if( ema3 > 49.0105 )
					if( tema <= 55.3501 )
						if( ema2 <= 52.4041 )
							if( ema13 <= 1.28647 )
								if( ema13 <= 0.59191 )
									ret := -0.260870
								if( ema13 > 0.59191 )
									ret := 0.302885
							if( ema13 > 1.28647 )
								if( ema13 <= 1.69137 )
									ret := -0.944444 // sell
								if( ema13 > 1.69137 )
									ret := 0.393939
						if( ema2 > 52.4041 )
							if( ema1 <= 54.3692 )
								if( ema12 <= 0.314359 )
									ret := 0.000000
								if( ema12 > 0.314359 )
									ret := -0.590909
							if( ema1 > 54.3692 )
								if( ema1 <= 54.9053 )
									ret := 0.128205
								if( ema1 > 54.9053 )
									ret := -0.900000 // sell
					if( tema > 55.3501 )
						if( ema13 <= 1.84955 )
							if( ema12 <= 0.510611 )
								if( ema1 <= 61.911 )
									ret := 0.389706
								if( ema1 > 61.911 )
									ret := 0.020633
							if( ema12 > 0.510611 )
								if( ema2 <= 74.8625 )
									ret := -0.224359
								if( ema2 > 74.8625 )
									ret := 0.386364
						if( ema13 > 1.84955 )
							if( ema1 <= 69.2855 )
								if( ema2 <= 62.3944 )
									ret := 0.676471
								if( ema2 > 62.3944 )
									ret := 1.000000 // buy
							if( ema1 > 69.2855 )
								if( ema3 <= 68.4583 )
									ret := -0.250000
								if( ema3 > 68.4583 )
									ret := 0.384615
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

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
float op_operation = decision_tree_0_SNAP_15Min_162559f4(ema1, tema, ema12, ema2, ema3, ema13)

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


