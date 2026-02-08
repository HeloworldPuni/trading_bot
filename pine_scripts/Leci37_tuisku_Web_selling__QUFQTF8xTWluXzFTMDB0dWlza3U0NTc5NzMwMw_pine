//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI
// ID_model: AAPL_1Min_1S00_45797303 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AAPL_1Min_1S00_45797303", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AAPL_1Min_45797303(rsi1, smoothK_k, d_k, k, d, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( rsi1 <= 42.6068 )
		if( rsi1 <= 29.5918 )
			if( k <= 75.8117 )
				if( smoothD_d <= 18.3409 )
					if( k <= 13.8772 )
						if( d <= 4.12466 )
							if( k <= 0.004558 )
								if( smoothD_d <= -2.47429 )
									ret := -0.165663
								if( smoothD_d > -2.47429 )
									ret := 0.008183
							if( k > 0.004558 )
								if( rsi1 <= 10.7423 )
									ret := 0.531532
								if( rsi1 > 10.7423 )
									ret := 0.036468
						if( d > 4.12466 )
							if( d_k <= 11.0409 )
								if( smoothD_d <= 7.53695 )
									ret := 0.190874
								if( smoothD_d > 7.53695 )
									ret := 0.006303
							if( d_k > 11.0409 )
								if( k <= 4.60328 )
									ret := 0.374286
								if( k > 4.60328 )
									ret := 0.725490 // buy
					if( k > 13.8772 )
						if( rsi1 <= 19.5972 )
							if( rsi1 <= 13.9729 )
								if( smoothD_d <= 13.1856 )
									ret := 0.040000
								if( smoothD_d > 13.1856 )
									ret := 0.821429 // buy
							if( rsi1 > 13.9729 )
								if( smoothD_d <= 11.3013 )
									ret := -0.733333 // sell
								if( smoothD_d > 11.3013 )
									ret := -0.216374
						if( rsi1 > 19.5972 )
							if( rsi1 <= 25.0099 )
								if( d <= 13.3878 )
									ret := 0.362676
								if( d > 13.3878 )
									ret := -0.021739
							if( rsi1 > 25.0099 )
								if( k <= 16.2502 )
									ret := -0.291498
								if( k > 16.2502 )
									ret := -0.015789
				if( smoothD_d > 18.3409 )
					if( d_k <= 17.7604 )
						if( d <= 31.1371 )
							if( d_k <= 16.6728 )
								if( smoothK_k <= 27.1079 )
									ret := 0.391941
								if( smoothK_k > 27.1079 )
									ret := 0.125413
							if( d_k > 16.6728 )
								if( k <= 11.6 )
									ret := -0.400000
								if( k > 11.6 )
									ret := -0.800000 // sell
						if( d > 31.1371 )
							if( rsi1 <= 24.1939 )
								if( k <= 19.9818 )
									ret := 0.950000 // buy
								if( k > 19.9818 )
									ret := -0.086181
							if( rsi1 > 24.1939 )
								if( d <= 33.1771 )
									ret := -0.267442
								if( d > 33.1771 )
									ret := 0.153135
					if( d_k > 17.7604 )
						if( d_k <= 29.8956 )
							if( smoothK_k <= 6.48885 )
								if( d_k <= 22.3632 )
									ret := 0.602740
								if( d_k > 22.3632 )
									ret := -0.139785
							if( smoothK_k > 6.48885 )
								if( smoothD_d <= 56.1109 )
									ret := 0.615591
								if( smoothD_d > 56.1109 )
									ret := 0.247126
						if( d_k > 29.8956 )
							if( d <= 47.0945 )
								if( d_k <= 31.0031 )
									ret := -0.157895
								if( d_k > 31.0031 )
									ret := -0.647059
							if( d > 47.0945 )
								if( d_k <= 32.358 )
									ret := -0.142857
								if( d_k > 32.358 )
									ret := 0.846154 // buy
			if( k > 75.8117 )
				if( d <= 65.2662 )
					if( smoothD_d <= 60.4498 )
						if( d_k <= -17.9084 )
							if( d_k <= -25.0089 )
								ret := 0.812500 // buy
							if( d_k > -25.0089 )
								ret := -0.111111
						if( d_k > -17.9084 )
							ret := 0.923077 // buy
					if( smoothD_d > 60.4498 )
						ret := 1.000000 // buy
				if( d > 65.2662 )
					if( d <= 78.6623 )
						if( rsi1 <= 28.5579 )
							if( smoothK_k <= 80.9228 )
								ret := -0.333333
							if( smoothK_k > 80.9228 )
								ret := -0.625000
						if( rsi1 > 28.5579 )
							ret := 0.333333
					if( d > 78.6623 )
						if( rsi1 <= 23.9214 )
							ret := 0.961538 // buy
						if( rsi1 > 23.9214 )
							if( smoothK_k <= 87.2664 )
								if( smoothK_k <= 82.7307 )
									ret := 0.486486
								if( smoothK_k > 82.7307 )
									ret := -0.785714 // sell
							if( smoothK_k > 87.2664 )
								if( rsi1 <= 28.5898 )
									ret := 0.461538
								if( rsi1 > 28.5898 )
									ret := 0.888889 // buy
		if( rsi1 > 29.5918 )
			if( d_k <= -6.63411 )
				if( smoothK_k <= 11.9992 )
					if( smoothD_d <= 1.24338 )
						ret := 0.285714
					if( smoothD_d > 1.24338 )
						if( d <= 7.05074 )
							if( k <= 13.7365 )
								if( d <= 5.24378 )
									ret := -0.756098 // sell
								if( d > 5.24378 )
									ret := -0.209677
							if( k > 13.7365 )
								if( smoothD_d <= 2.53662 )
									ret := -0.454545
								if( smoothD_d > 2.53662 )
									ret := -0.782609 // sell
						if( d > 7.05074 )
							ret := 0.000000
				if( smoothK_k > 11.9992 )
					if( rsi1 <= 32.7306 )
						if( smoothK_k <= 14.7128 )
							if( smoothK_k <= 13.7006 )
								ret := -0.235294
							if( smoothK_k > 13.7006 )
								if( smoothK_k <= 14.1518 )
									ret := -0.909091 // sell
								if( smoothK_k > 14.1518 )
									ret := -0.769231 // sell
						if( smoothK_k > 14.7128 )
							if( k <= 69.2008 )
								if( d <= 38.8853 )
									ret := 0.304042
								if( d > 38.8853 )
									ret := -0.366071
							if( k > 69.2008 )
								if( k <= 90.9788 )
									ret := 0.672727
								if( k > 90.9788 )
									ret := 0.058824
					if( rsi1 > 32.7306 )
						if( d <= 9.55716 )
							if( k <= 22.3475 )
								if( rsi1 <= 34.8814 )
									ret := 0.538462
								if( rsi1 > 34.8814 )
									ret := 0.162162
							if( k > 22.3475 )
								if( d <= 9.06702 )
									ret := 1.000000 // buy
								if( d > 9.06702 )
									ret := 0.555556
						if( d > 9.55716 )
							if( d_k <= -25.7753 )
								if( smoothD_d <= 55.8855 )
									ret := -0.310127
								if( smoothD_d > 55.8855 )
									ret := -0.736842 // sell
							if( d_k > -25.7753 )
								if( d <= 33.0499 )
									ret := -0.152274
								if( d > 33.0499 )
									ret := 0.006464
			if( d_k > -6.63411 )
				if( smoothK_k <= 25.2453 )
					if( d_k <= -5.51878 )
						if( k <= 17.637 )
							if( smoothK_k <= 7.83082 )
								if( k <= 10.1354 )
									ret := 0.492754
								if( k > 10.1354 )
									ret := -0.324324
							if( smoothK_k > 7.83082 )
								if( d_k <= -6.36639 )
									ret := 0.764706 // buy
								if( d_k > -6.36639 )
									ret := 0.422360
						if( k > 17.637 )
							if( smoothD_d <= 14.4838 )
								if( smoothD_d <= 12.8602 )
									ret := 0.164557
								if( smoothD_d > 12.8602 )
									ret := -0.774194 // sell
							if( smoothD_d > 14.4838 )
								if( smoothD_d <= 15.0456 )
									ret := 1.000000 // buy
								if( smoothD_d > 15.0456 )
									ret := 0.378378
					if( d_k > -5.51878 )
						if( rsi1 <= 31.1642 )
							if( smoothD_d <= 22.0566 )
								if( smoothK_k <= 4.58249 )
									ret := -0.007587
								if( smoothK_k > 4.58249 )
									ret := -0.328042
							if( smoothD_d > 22.0566 )
								if( k <= 26.1416 )
									ret := 0.144385
								if( k > 26.1416 )
									ret := 0.794872 // buy
						if( rsi1 > 31.1642 )
							if( d <= 2.50597 )
								if( smoothD_d <= -2.98902 )
									ret := 0.347418
								if( smoothD_d > -2.98902 )
									ret := -0.066358
							if( d > 2.50597 )
								if( d_k <= 28.929 )
									ret := 0.106876
								if( d_k > 28.929 )
									ret := -0.233333
				if( smoothK_k > 25.2453 )
					if( d <= 27.5386 )
						if( smoothD_d <= 23.0793 )
							if( d <= 24.2101 )
								if( k <= 28.9952 )
									ret := 0.117647
								if( k > 28.9952 )
									ret := -0.863636 // sell
							if( d > 24.2101 )
								if( smoothK_k <= 26.515 )
									ret := 0.733333 // buy
								if( smoothK_k > 26.515 )
									ret := 0.073171
						if( smoothD_d > 23.0793 )
							if( smoothK_k <= 26.942 )
								if( smoothD_d <= 23.965 )
									ret := -0.566667
								if( smoothD_d > 23.965 )
									ret := 0.181818
							if( smoothK_k > 26.942 )
								if( rsi1 <= 34.4715 )
									ret := -0.181818
								if( rsi1 > 34.4715 )
									ret := -0.763636 // sell
					if( d > 27.5386 )
						if( smoothK_k <= 96.2235 )
							if( d_k <= 22.2333 )
								if( k <= 98.7095 )
									ret := 0.006265
								if( k > 98.7095 )
									ret := -0.703704 // sell
							if( d_k > 22.2333 )
								if( rsi1 <= 31.956 )
									ret := -0.641791
								if( rsi1 > 31.956 )
									ret := 0.338095
						if( smoothK_k > 96.2235 )
							if( k <= 99.9311 )
								if( rsi1 <= 40.1681 )
									ret := 0.847826 // buy
								if( rsi1 > 40.1681 )
									ret := 0.200000
							if( k > 99.9311 )
								if( d <= 97.2296 )
									ret := 0.333333
								if( d > 97.2296 )
									ret := -0.200000
	if( rsi1 > 42.6068 )
		if( d <= 1.34316 )
			if( d <= 0.753707 )
				if( rsi1 <= 50.5189 )
					if( d_k <= -0.09003 )
						if( smoothD_d <= -2.57701 )
							if( k <= 0.583863 )
								ret := -0.636364
							if( k > 0.583863 )
								ret := -0.916667 // sell
						if( smoothD_d > -2.57701 )
							if( d <= 0.575987 )
								ret := -0.210526
							if( d > 0.575987 )
								ret := -0.600000
					if( d_k > -0.09003 )
						if( d <= 0.033905 )
							ret := -0.088235
						if( d > 0.033905 )
							if( k <= 0.23326 )
								if( rsi1 <= 46.8764 )
									ret := 0.562500
								if( rsi1 > 46.8764 )
									ret := 0.863636 // buy
							if( k > 0.23326 )
								ret := 0.083333
				if( rsi1 > 50.5189 )
					if( d_k <= -0.130608 )
						ret := 0.000000
					if( d_k > -0.130608 )
						if( rsi1 <= 57.7475 )
							if( smoothK_k <= -2.84648 )
								if( smoothD_d <= -2.93069 )
									ret := 0.777778 // buy
								if( smoothD_d > -2.93069 )
									ret := 0.400000
							if( smoothK_k > -2.84648 )
								ret := 0.444444
						if( rsi1 > 57.7475 )
							if( d <= 0.015915 )
								ret := 0.785714 // buy
							if( d > 0.015915 )
								ret := 1.000000 // buy
			if( d > 0.753707 )
				if( k <= 3.52039 )
					if( d_k <= 1.23332 )
						if( rsi1 <= 49.8039 )
							if( d_k <= 0.26221 )
								if( d_k <= -0.257676 )
									ret := 0.178571
								if( d_k > -0.257676 )
									ret := -0.916667 // sell
							if( d_k > 0.26221 )
								if( smoothD_d <= -2.21223 )
									ret := 0.444444
								if( smoothD_d > -2.21223 )
									ret := 0.827586 // buy
						if( rsi1 > 49.8039 )
							if( rsi1 <= 54.8649 )
								if( smoothK_k <= -1.77298 )
									ret := 1.000000 // buy
								if( smoothK_k > -1.77298 )
									ret := 0.708333 // buy
							if( rsi1 > 54.8649 )
								if( smoothD_d <= -1.91329 )
									ret := 0.681818
								if( smoothD_d > -1.91329 )
									ret := 0.190476
					if( d_k > 1.23332 )
						ret := 0.071429
				if( k > 3.52039 )
					ret := -0.800000 // sell
		if( d > 1.34316 )
			if( d_k <= 30.8468 )
				if( rsi1 <= 80.1486 )
					if( rsi1 <= 79.9147 )
						if( smoothK_k <= -2.74268 )
							if( d <= 4.24637 )
								if( smoothD_d <= 0.824654 )
									ret := 0.302326
								if( smoothD_d > 0.824654 )
									ret := 0.761905 // buy
							if( d > 4.24637 )
								if( rsi1 <= 44.6506 )
									ret := -0.487179
								if( rsi1 > 44.6506 )
									ret := 0.084633
						if( smoothK_k > -2.74268 )
							if( d <= 1.61202 )
								if( rsi1 <= 56.915 )
									ret := -0.413043
								if( rsi1 > 56.915 )
									ret := -0.954545 // sell
							if( d > 1.61202 )
								if( k <= 38.6856 )
									ret := -0.048521
								if( k > 38.6856 )
									ret := -0.021679
					if( rsi1 > 79.9147 )
						if( smoothD_d <= 53.6223 )
							ret := -0.571429
						if( smoothD_d > 53.6223 )
							if( rsi1 <= 80.0728 )
								if( smoothD_d <= 78.5361 )
									ret := 0.814815 // buy
								if( smoothD_d > 78.5361 )
									ret := 0.081081
							if( rsi1 > 80.0728 )
								if( smoothD_d <= 92.1339 )
									ret := 0.769231 // buy
								if( smoothD_d > 92.1339 )
									ret := 0.333333
				if( rsi1 > 80.1486 )
					if( d_k <= 0.261397 )
						if( k <= 82.4758 )
							if( k <= 71.8178 )
								if( smoothK_k <= 32.4851 )
									ret := 0.821429 // buy
								if( smoothK_k > 32.4851 )
									ret := -0.300000
							if( k > 71.8178 )
								if( smoothK_k <= 76.8481 )
									ret := 0.253086
								if( smoothK_k > 76.8481 )
									ret := 0.647887
						if( k > 82.4758 )
							if( k <= 87.2545 )
								if( d_k <= -4.33338 )
									ret := -0.625000
								if( d_k > -4.33338 )
									ret := 0.085106
							if( k > 87.2545 )
								if( d <= 85.781 )
									ret := -0.025424
								if( d > 85.781 )
									ret := -0.210570
					if( d_k > 0.261397 )
						if( d <= 95.671 )
							if( smoothK_k <= 80.9004 )
								if( smoothD_d <= 85.7701 )
									ret := 0.135632
								if( smoothD_d > 85.7701 )
									ret := -0.541667
							if( smoothK_k > 80.9004 )
								if( d <= 90.0915 )
									ret := -0.658537
								if( d > 90.0915 )
									ret := -0.279255
						if( d > 95.671 )
							if( d_k <= 0.275942 )
								ret := 0.866667 // buy
							if( d_k > 0.275942 )
								if( rsi1 <= 86.6552 )
									ret := 0.110701
								if( rsi1 > 86.6552 )
									ret := 0.526946
			if( d_k > 30.8468 )
				if( d <= 57.985 )
					if( smoothK_k <= 6.75072 )
						if( k <= 2.13082 )
							ret := 0.200000
						if( k > 2.13082 )
							ret := 0.785714 // buy
					if( smoothK_k > 6.75072 )
						if( k <= 13.359 )
							ret := -0.857143 // sell
						if( k > 13.359 )
							if( rsi1 <= 50.3095 )
								ret := 0.043478
							if( rsi1 > 50.3095 )
								if( d_k <= 31.8742 )
									ret := 0.384615
								if( d_k > 31.8742 )
									ret := 0.625000
				if( d > 57.985 )
					if( smoothD_d <= 60.8653 )
						if( rsi1 <= 51.1133 )
							if( smoothK_k <= 25.8459 )
								ret := 0.538462
							if( smoothK_k > 25.8459 )
								ret := 1.000000 // buy
						if( rsi1 > 51.1133 )
							ret := 1.000000 // buy
					if( smoothD_d > 60.8653 )
						if( k <= 33.3636 )
							ret := -0.125000
						if( k > 33.3636 )
							ret := 0.769231 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Stochastic_RSI 
//@version=5
//indicator title="Stochastic RSI", shorttitle="Stoch RSI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
smoothK = input.int(3, "K", minval=1)
smoothD = input.int(3, "D", minval=1)
lengthRSI = input.int(14, "RSI Length", minval=1)
lengthStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)
plot(k, "K", color=#2962FF)
plot(d, "D", color=#FF6D00)

d_k = d - k
smoothD_d = d - smoothD
smoothK_k = k - smoothK

h0 = hline(80, "Upper Band", color=#787B86)
hline(50, "Middle Band", color=color.new(#787B86, 50))
h1 = hline(20, "Lower Band", color=#787B86)
fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")
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
float op_operation = decision_tree_0_AAPL_1Min_45797303(rsi1, smoothK_k, d_k, k, d, smoothD_d)

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


