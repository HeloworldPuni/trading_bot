//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI
// ID_model: RBLX_1Hour_1S00_4a0710fb Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RBLX_1Hour_1S00_4a0710fb", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RBLX_1Hour_4a0710fb(rsi1, d, k, smoothD_d, d_k, smoothK_k)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( rsi1 <= 34 )
		if( d_k <= 22.7382 )
			if( smoothK_k <= -2.62487 )
				if( d <= 2.85202 )
					if( d_k <= 0.006555 )
						if( rsi1 <= 8.14438 )
							ret := 0.000000
						if( rsi1 > 8.14438 )
							ret := -0.486111
					if( d_k > 0.006555 )
						if( rsi1 <= 4.36974 )
							ret := -1.000000 // sell
						if( rsi1 > 4.36974 )
							ret := 0.073171
				if( d > 2.85202 )
					if( k <= 4.1e-05 )
						if( rsi1 <= 23.1178 )
							ret := -0.454545
						if( rsi1 > 23.1178 )
							ret := -0.767442 // sell
					if( k > 4.1e-05 )
						if( d_k <= 6.76716 )
							ret := -0.730769 // sell
						if( d_k > 6.76716 )
							ret := 0.666667
			if( smoothK_k > -2.62487 )
				if( rsi1 <= 15.1669 )
					if( k <= 1.09167 )
						if( rsi1 <= 11.538 )
							ret := -0.814815 // sell
						if( rsi1 > 11.538 )
							ret := -0.071429
					if( k > 1.09167 )
						if( d_k <= 3.3449 )
							ret := 0.242991
						if( d_k > 3.3449 )
							ret := 0.744681 // buy
				if( rsi1 > 15.1669 )
					if( d_k <= -22.0477 )
						if( smoothD_d <= 27.9955 )
							ret := -0.800000 // sell
						if( smoothD_d > 27.9955 )
							ret := -0.463415
					if( d_k > -22.0477 )
						if( d <= 16.9423 )
							ret := -0.038764
						if( d > 16.9423 )
							ret := -0.160776
		if( d_k > 22.7382 )
			if( k <= 48.6572 )
				if( d <= 69.5368 )
					if( smoothK_k <= 14.8542 )
						if( smoothK_k <= -1.98334 )
							ret := 0.125000
						if( smoothK_k > -1.98334 )
							ret := 0.634615
					if( smoothK_k > 14.8542 )
						if( smoothD_d <= 57.0108 )
							ret := -0.257143
						if( smoothD_d > 57.0108 )
							ret := 0.434783
				if( d > 69.5368 )
					ret := 1.000000 // buy
			if( k > 48.6572 )
				ret := -0.285714
	if( rsi1 > 34 )
		if( rsi1 <= 49.8889 )
			if( smoothK_k <= 91.1391 )
				if( d_k <= -22.3223 )
					if( d <= 39.1853 )
						if( d_k <= -23.9802 )
							ret := -0.368421
						if( d_k > -23.9802 )
							ret := -0.837838 // sell
					if( d > 39.1853 )
						if( d <= 44.1534 )
							ret := 0.722222 // buy
						if( d > 44.1534 )
							ret := -0.507937
				if( d_k > -22.3223 )
					if( d_k <= 17.1366 )
						if( d_k <= -17.2605 )
							ret := 0.326531
						if( d_k > -17.2605 )
							ret := 0.111295
					if( d_k > 17.1366 )
						if( rsi1 <= 38.8851 )
							ret := 0.271429
						if( rsi1 > 38.8851 )
							ret := -0.178082
			if( smoothK_k > 91.1391 )
				if( rsi1 <= 47.8452 )
					if( d_k <= -12.0059 )
						if( smoothD_d <= 79.844 )
							ret := -0.240000
						if( smoothD_d > 79.844 )
							ret := 0.200000
					if( d_k > -12.0059 )
						if( d <= 90.8593 )
							ret := -0.804878 // sell
						if( d > 90.8593 )
							ret := -0.376000
				if( rsi1 > 47.8452 )
					if( rsi1 <= 48.441 )
						if( k <= 97.9246 )
							ret := 0.800000 // buy
						if( k > 97.9246 )
							ret := 0.500000
					if( rsi1 > 48.441 )
						if( d_k <= -7.52499 )
							ret := 0.300000
						if( d_k > -7.52499 )
							ret := -0.392857
		if( rsi1 > 49.8889 )
			if( smoothD_d <= 14.0894 )
				if( rsi1 <= 69.2186 )
					if( rsi1 <= 56.074 )
						if( rsi1 <= 51.4641 )
							ret := 0.025641
						if( rsi1 > 51.4641 )
							ret := -0.436123
					if( rsi1 > 56.074 )
						if( smoothK_k <= 18.3255 )
							ret := 0.170732
						if( smoothK_k > 18.3255 )
							ret := -0.607143
				if( rsi1 > 69.2186 )
					if( smoothK_k <= 22.5446 )
						if( k <= 14.9023 )
							ret := -0.877193 // sell
						if( k > 14.9023 )
							ret := -0.500000
					if( smoothK_k > 22.5446 )
						ret := 0.222222
			if( smoothD_d > 14.0894 )
				if( k <= 99.5999 )
					if( smoothD_d <= 94.1224 )
						if( rsi1 <= 73.8132 )
							ret := 0.018237
						if( rsi1 > 73.8132 )
							ret := -0.090909
					if( smoothD_d > 94.1224 )
						if( d_k <= 2.86436 )
							ret := 0.248050
						if( d_k > 2.86436 )
							ret := -0.301587
				if( k > 99.5999 )
					if( smoothD_d <= 96.9382 )
						if( smoothD_d <= 86.8614 )
							ret := 0.124183
						if( smoothD_d > 86.8614 )
							ret := -0.302326
					if( smoothD_d > 96.9382 )
						if( rsi1 <= 77.4465 )
							ret := 0.636364
						if( rsi1 > 77.4465 )
							ret := -0.125000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_RBLX_1Hour_4a0710fb(rsi1, d, k, smoothD_d, d_k, smoothK_k)

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


