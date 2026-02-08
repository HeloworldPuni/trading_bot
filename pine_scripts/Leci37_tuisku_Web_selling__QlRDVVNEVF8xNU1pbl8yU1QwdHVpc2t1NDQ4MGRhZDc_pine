//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: BTCUSDT_15Min_2ST0_4480dad7 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_BTCUSDT_15Min_2ST0_4480dad7", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_BTCUSDT_15Min_4480dad7(rsi1, smoothK_k, d_k, k, d, smoothD_d, ema3, tema, ema2, ema12, ema13, ema1)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.5,min_samples_leaf=4, random_state=843828734)
	if( smoothK_k <= 53.8283 )
		if( ema1 <= 25815.7 )
			if( rsi1 <= 31.1771 )
				if( d <= 0.198921 )
					if( ema3 <= 19454.5 )
						if( ema2 <= 18541.2 )
							ret := 0.000000
						if( ema2 > 18541.2 )
							if( ema2 <= 19125.4 )
								ret := 1.000000 // buy
							if( ema2 > 19125.4 )
								ret := 0.400000
					if( ema3 > 19454.5 )
						if( ema13 <= -371.431 )
							if( rsi1 <= 7.2916 )
								ret := -0.600000
							if( rsi1 > 7.2916 )
								ret := -0.979167 // sell
						if( ema13 > -371.431 )
							if( ema12 <= -159.733 )
								ret := 0.428571
							if( ema12 > -159.733 )
								ret := -0.526316
				if( d > 0.198921 )
					if( ema13 <= -45.6663 )
						if( ema13 <= -177.62 )
							if( ema13 <= -622.521 )
								ret := 0.763158 // buy
							if( ema13 > -622.521 )
								ret := 0.005686
						if( ema13 > -177.62 )
							if( ema1 <= 16492.5 )
								ret := -0.314286
							if( ema1 > 16492.5 )
								ret := 0.273363
					if( ema13 > -45.6663 )
						if( ema1 <= 22875.9 )
							if( smoothD_d <= 0.546471 )
								ret := -0.361446
							if( smoothD_d > 0.546471 )
								ret := 0.075000
						if( ema1 > 22875.9 )
							if( ema3 <= 25605.7 )
								ret := -0.406593
							if( ema3 > 25605.7 )
								ret := -0.775862 // sell
			if( rsi1 > 31.1771 )
				if( d_k <= 20.2913 )
					if( tema <= 19237.1 )
						if( tema <= 18621.1 )
							if( tema <= 18197.4 )
								ret := -0.033719
							if( tema > 18197.4 )
								ret := -0.793814 // sell
						if( tema > 18621.1 )
							if( ema2 <= 18825.8 )
								ret := 0.810811 // buy
							if( ema2 > 18825.8 )
								ret := 0.121049
					if( tema > 19237.1 )
						if( k <= 37.7166 )
							if( ema2 <= 23501.6 )
								ret := -0.135577
							if( ema2 > 23501.6 )
								ret := 0.014375
						if( k > 37.7166 )
							if( tema <= 19887.6 )
								ret := -0.280435
							if( tema > 19887.6 )
								ret := 0.025458
				if( d_k > 20.2913 )
					if( rsi1 <= 56.8126 )
						if( ema12 <= -53.837 )
							if( d <= 31.3709 )
								ret := -1.000000 // sell
							if( d > 31.3709 )
								ret := 0.813953 // buy
						if( ema12 > -53.837 )
							if( ema2 <= 24699.6 )
								ret := 0.044554
							if( ema2 > 24699.6 )
								ret := -0.413793
					if( rsi1 > 56.8126 )
						if( ema3 <= 23053.2 )
							if( ema2 <= 22073.5 )
								ret := 0.451852
							if( ema2 > 22073.5 )
								ret := 0.916667 // buy
						if( ema3 > 23053.2 )
							if( tema <= 24033.2 )
								ret := -0.266667
							if( tema > 24033.2 )
								ret := 0.533333
		if( ema1 > 25815.7 )
			if( d <= 17.595 )
				if( rsi1 <= 36.9183 )
					if( ema3 <= 39791.2 )
						if( ema12 <= -58.3462 )
							if( rsi1 <= 27.8013 )
								ret := -0.279539
							if( rsi1 > 27.8013 )
								ret := 0.065817
						if( ema12 > -58.3462 )
							if( ema12 <= 4.20771 )
								ret := -0.576772
							if( ema12 > 4.20771 )
								ret := -0.822995 // sell
					if( ema3 > 39791.2 )
						if( rsi1 <= 27.539 )
							if( ema12 <= -269.217 )
								ret := -0.777174 // sell
							if( ema12 > -269.217 )
								ret := -0.880379 // sell
						if( rsi1 > 27.539 )
							if( ema13 <= 1.47186 )
								ret := -0.604575
							if( ema13 > 1.47186 )
								ret := -0.832406 // sell
				if( rsi1 > 36.9183 )
					if( ema13 <= 29.8589 )
						if( ema13 <= -295.623 )
							if( ema2 <= 46388.6 )
								ret := 0.300000
							if( ema2 > 46388.6 )
								ret := 0.750000 // buy
						if( ema13 > -295.623 )
							if( ema12 <= -46.1398 )
								ret := 0.093700
							if( ema12 > -46.1398 )
								ret := -0.207723
					if( ema13 > 29.8589 )
						if( rsi1 <= 48.519 )
							if( ema13 <= 51.9806 )
								ret := -0.434470
							if( ema13 > 51.9806 )
								ret := -0.662695
						if( rsi1 > 48.519 )
							if( ema12 <= 78.9728 )
								ret := -0.006452
							if( ema12 > 78.9728 )
								ret := -0.335659
			if( d > 17.595 )
				if( k <= 26.2231 )
					if( ema12 <= 13.6682 )
						if( rsi1 <= 37.8817 )
							if( tema <= 39865.4 )
								ret := -0.300083
							if( tema > 39865.4 )
								ret := -0.571209
						if( rsi1 > 37.8817 )
							if( ema13 <= 35.0549 )
								ret := -0.007277
							if( ema13 > 35.0549 )
								ret := 0.459119
					if( ema12 > 13.6682 )
						if( rsi1 <= 56.85 )
							if( ema12 <= 51.9387 )
								ret := -0.511506
							if( ema12 > 51.9387 )
								ret := -0.690073
						if( rsi1 > 56.85 )
							if( ema12 <= 91.6996 )
								ret := 0.254190
							if( ema12 > 91.6996 )
								ret := -0.158520
				if( k > 26.2231 )
					if( ema12 <= -122.638 )
						if( ema13 <= -287.472 )
							if( tema <= 30883 )
								ret := 0.400000
							if( tema > 30883 )
								ret := -0.111446
						if( ema13 > -287.472 )
							if( ema13 <= -201.972 )
								ret := 0.354779
							if( ema13 > -201.972 )
								ret := 0.657895
					if( ema12 > -122.638 )
						if( rsi1 <= 54.5186 )
							if( rsi1 <= 38.2502 )
								ret := -0.501001
							if( rsi1 > 38.2502 )
								ret := -0.184476
						if( rsi1 > 54.5186 )
							if( ema12 <= 158.42 )
								ret := 0.285352
							if( ema12 > 158.42 )
								ret := -0.151369
	if( smoothK_k > 53.8283 )
		if( tema <= 25424.3 )
			if( tema <= 23909.9 )
				if( ema2 <= 23750.4 )
					if( ema2 <= 23436.7 )
						if( rsi1 <= 87.1653 )
							if( k <= 90.859 )
								ret := 0.048562
							if( k > 90.859 )
								ret := -0.080690
						if( rsi1 > 87.1653 )
							if( ema3 <= 19672 )
								ret := 0.690647
							if( ema3 > 19672 )
								ret := 0.221053
					if( ema2 > 23436.7 )
						if( ema1 <= 23564.8 )
							if( smoothK_k <= 71.5466 )
								ret := -0.425926
							if( smoothK_k > 71.5466 )
								ret := -0.804688 // sell
						if( ema1 > 23564.8 )
							if( rsi1 <= 67.1294 )
								ret := 0.180180
							if( rsi1 > 67.1294 )
								ret := -0.500000
				if( ema2 > 23750.4 )
					if( smoothK_k <= 89.7054 )
						if( ema12 <= 35.1949 )
							if( ema3 <= 23785.4 )
								ret := 0.939394 // buy
							if( ema3 > 23785.4 )
								ret := 0.536458
						if( ema12 > 35.1949 )
							ret := -0.500000
					if( smoothK_k > 89.7054 )
						if( ema3 <= 23921.3 )
							if( rsi1 <= 51.3722 )
								ret := 0.500000
							if( rsi1 > 51.3722 )
								ret := -0.045455
						if( ema3 > 23921.3 )
							if( smoothK_k <= 93.8563 )
								ret := 1.000000 // buy
							if( smoothK_k > 93.8563 )
								ret := 0.500000
			if( tema > 23909.9 )
				if( rsi1 <= 71.6322 )
					if( ema1 <= 24234.6 )
						if( smoothK_k <= 70.5113 )
							if( tema <= 24164 )
								ret := -0.122642
							if( tema > 24164 )
								ret := -0.848485 // sell
						if( smoothK_k > 70.5113 )
							if( ema2 <= 24141.5 )
								ret := -0.593985
							if( ema2 > 24141.5 )
								ret := -0.928571 // sell
					if( ema1 > 24234.6 )
						if( tema <= 24356.7 )
							if( d_k <= 9.51015 )
								ret := 0.783784 // buy
							if( d_k > 9.51015 )
								ret := -0.333333
						if( tema > 24356.7 )
							if( smoothD_d <= 58.1493 )
								ret := 0.183486
							if( smoothD_d > 58.1493 )
								ret := -0.382403
				if( rsi1 > 71.6322 )
					if( ema2 <= 24974.5 )
						if( ema2 <= 24489.4 )
							if( d_k <= 3.63882 )
								ret := -0.103960
							if( d_k > 3.63882 )
								ret := 0.542373
						if( ema2 > 24489.4 )
							if( smoothK_k <= 70.0527 )
								ret := 0.400000
							if( smoothK_k > 70.0527 )
								ret := -0.745098 // sell
					if( ema2 > 24974.5 )
						if( ema12 <= 62.8733 )
							ret := 1.000000 // buy
						if( ema12 > 62.8733 )
							ret := 0.750000 // buy
		if( tema > 25424.3 )
			if( smoothK_k <= 72.2109 )
				if( rsi1 <= 59.7839 )
					if( ema12 <= 14.5329 )
						if( ema12 <= -32.8892 )
							if( rsi1 <= 46.0331 )
								ret := 0.010708
							if( rsi1 > 46.0331 )
								ret := 0.733709 // buy
						if( ema12 > -32.8892 )
							if( ema13 <= -51.7683 )
								ret := -0.200535
							if( ema13 > -51.7683 )
								ret := 0.121103
					if( ema12 > 14.5329 )
						if( rsi1 <= 55.0115 )
							if( ema12 <= 78.1551 )
								ret := -0.438867
							if( ema12 > 78.1551 )
								ret := -0.778409 // sell
						if( rsi1 > 55.0115 )
							if( ema12 <= 82.29 )
								ret := -0.018786
							if( ema12 > 82.29 )
								ret := -0.552301
				if( rsi1 > 59.7839 )
					if( tema <= 33223.2 )
						if( tema <= 31370.8 )
							if( d <= 78.0169 )
								ret := 0.237632
							if( d > 78.0169 )
								ret := 0.559633
						if( tema > 31370.8 )
							if( smoothD_d <= 79.5013 )
								ret := -0.820513 // sell
							if( smoothD_d > 79.5013 )
								ret := 0.000000
					if( tema > 33223.2 )
						if( ema13 <= 399.193 )
							if( ema13 <= 46.6936 )
								ret := 0.717017 // buy
							if( ema13 > 46.6936 )
								ret := 0.482143
						if( ema13 > 399.193 )
							if( d <= 74.7861 )
								ret := -0.077273
							if( d > 74.7861 )
								ret := 0.541935
			if( smoothK_k > 72.2109 )
				if( rsi1 <= 67.6546 )
					if( ema12 <= -11.3438 )
						if( ema1 <= 35434.8 )
							if( tema <= 35348.9 )
								ret := 0.371997
							if( tema > 35348.9 )
								ret := -1.000000 // sell
						if( ema1 > 35434.8 )
							if( rsi1 <= 46.2684 )
								ret := 0.078492
							if( rsi1 > 46.2684 )
								ret := 0.688665
					if( ema12 > -11.3438 )
						if( rsi1 <= 59.5078 )
							if( rsi1 <= 55.2927 )
								ret := -0.180137
							if( rsi1 > 55.2927 )
								ret := 0.041867
						if( rsi1 > 59.5078 )
							if( ema12 <= 48.5206 )
								ret := 0.416775
							if( ema12 > 48.5206 )
								ret := 0.116707
				if( rsi1 > 67.6546 )
					if( ema3 <= 34729.5 )
						if( rsi1 <= 75.3752 )
							if( ema13 <= 75.7097 )
								ret := 0.553191
							if( ema13 > 75.7097 )
								ret := 0.133056
						if( rsi1 > 75.3752 )
							if( ema13 <= 341.947 )
								ret := 0.738340 // buy
							if( ema13 > 341.947 )
								ret := -0.133005
					if( ema3 > 34729.5 )
						if( ema13 <= 729.228 )
							if( rsi1 <= 77.84 )
								ret := 0.740232 // buy
							if( rsi1 > 77.84 )
								ret := 0.850950 // buy
						if( ema13 > 729.228 )
							if( ema2 <= 64585 )
								ret := 0.145833
							if( ema2 > 64585 )
								ret := 0.887640 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
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
float op_operation = decision_tree_0_BTCUSDT_15Min_4480dad7(rsi1, smoothK_k, d_k, k, d, smoothD_d, ema3, tema, ema2, ema12, ema13, ema1)

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


