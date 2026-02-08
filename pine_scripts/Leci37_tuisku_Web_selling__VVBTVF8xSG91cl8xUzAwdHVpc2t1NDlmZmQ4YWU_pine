//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI
// ID_model: UPST_1Hour_1S00_49ffd8ae Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_UPST_1Hour_1S00_49ffd8ae", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_UPST_1Hour_49ffd8ae(rsi1, d, k, smoothD_d, d_k, smoothK_k)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6,max_features=sqrt, min_samples_split=10,random_state=843828734)
	if( rsi1 <= 46.4577 )
		if( smoothD_d <= 44.2775 )
			if( smoothD_d <= 34.6493 )
				if( smoothK_k <= 38.0585 )
					if( rsi1 <= 23.9911 )
						if( d <= 28.0547 )
							ret := -0.172287
						if( d > 28.0547 )
							ret := -0.500000
					if( rsi1 > 23.9911 )
						if( smoothK_k <= 2.3756 )
							ret := -0.011914
						if( smoothK_k > 2.3756 )
							ret := -0.138103
				if( smoothK_k > 38.0585 )
					if( d_k <= -11.538 )
						if( smoothD_d <= 32.6976 )
							ret := 0.113300
						if( smoothD_d > 32.6976 )
							ret := -0.290909
					if( d_k > -11.538 )
						if( k <= 43.5748 )
							ret := 0.740741 // buy
						if( k > 43.5748 )
							ret := 0.956522 // buy
			if( smoothD_d > 34.6493 )
				if( smoothK_k <= 53.8903 )
					if( smoothD_d <= 39.9666 )
						if( smoothK_k <= 20.9675 )
							ret := -0.662162
						if( smoothK_k > 20.9675 )
							ret := -0.187500
					if( smoothD_d > 39.9666 )
						if( rsi1 <= 41.2934 )
							ret := -0.125000
						if( rsi1 > 41.2934 )
							ret := 0.380952
				if( smoothK_k > 53.8903 )
					if( smoothK_k <= 61.6027 )
						if( smoothD_d <= 43.6369 )
							ret := -0.883117 // sell
						if( smoothD_d > 43.6369 )
							ret := 0.000000
					if( smoothK_k > 61.6027 )
						if( d_k <= -27.0961 )
							ret := -0.400000
						if( d_k > -27.0961 )
							ret := 0.608696
		if( smoothD_d > 44.2775 )
			if( d_k <= -0.427166 )
				if( smoothD_d <= 51.2153 )
					if( smoothK_k <= 53.1267 )
						if( smoothD_d <= 44.4844 )
							ret := -0.250000
						if( smoothD_d > 44.4844 )
							ret := 0.688889
					if( smoothK_k > 53.1267 )
						if( k <= 59.8279 )
							ret := -0.333333
						if( k > 59.8279 )
							ret := 0.271739
				if( smoothD_d > 51.2153 )
					if( d <= 61.8377 )
						if( smoothD_d <= 53.3764 )
							ret := -0.085714
						if( smoothD_d > 53.3764 )
							ret := -0.512000
					if( d > 61.8377 )
						if( rsi1 <= 41.1896 )
							ret := 0.045714
						if( rsi1 > 41.1896 )
							ret := -0.180077
			if( d_k > -0.427166 )
				if( rsi1 <= 42.535 )
					if( d_k <= 4.35524 )
						if( k <= 99.147 )
							ret := 0.248521
						if( k > 99.147 )
							ret := -0.500000
					if( d_k > 4.35524 )
						if( smoothK_k <= 80.4602 )
							ret := 0.001385
						if( smoothK_k > 80.4602 )
							ret := -0.630435
				if( rsi1 > 42.535 )
					if( k <= 69.3516 )
						if( smoothK_k <= 52.5692 )
							ret := 0.178571
						if( smoothK_k > 52.5692 )
							ret := -0.092105
					if( k > 69.3516 )
						if( k <= 81.7768 )
							ret := 0.506024
						if( k > 81.7768 )
							ret := 0.225806
	if( rsi1 > 46.4577 )
		if( smoothK_k <= 96.979 )
			if( k <= 97.1038 )
				if( d_k <= -8.5312 )
					if( smoothK_k <= 25.9939 )
						if( k <= 25.3827 )
							ret := 0.271186
						if( k > 25.3827 )
							ret := -0.540000
					if( smoothK_k > 25.9939 )
						if( rsi1 <= 79.1431 )
							ret := 0.255432
						if( rsi1 > 79.1431 )
							ret := -0.286957
				if( d_k > -8.5312 )
					if( d <= 7.85645 )
						if( d_k <= -4.91852 )
							ret := -0.333333
						if( d_k > -4.91852 )
							ret := 0.405556
					if( d > 7.85645 )
						if( rsi1 <= 71.8029 )
							ret := 0.031028
						if( rsi1 > 71.8029 )
							ret := -0.072277
			if( k > 97.1038 )
				if( rsi1 <= 84.5918 )
					if( rsi1 <= 71.2399 )
						if( smoothK_k <= 95.5837 )
							ret := 0.328125
						if( smoothK_k > 95.5837 )
							ret := -0.071970
					if( rsi1 > 71.2399 )
						if( rsi1 <= 82.7037 )
							ret := 0.371345
						if( rsi1 > 82.7037 )
							ret := 0.734940 // buy
				if( rsi1 > 84.5918 )
					if( smoothK_k <= 96.9365 )
						if( d <= 99.5092 )
							ret := -0.100000
						if( d > 99.5092 )
							ret := -0.608696
					if( smoothK_k > 96.9365 )
						if( rsi1 <= 86.1775 )
							ret := -1.000000 // sell
						if( rsi1 > 86.1775 )
							ret := 1.000000 // buy
		if( smoothK_k > 96.979 )
			if( d_k <= -11.3473 )
				if( smoothD_d <= 82.6787 )
					if( d_k <= -15.3669 )
						if( rsi1 <= 68.1967 )
							ret := -0.675000
						if( rsi1 > 68.1967 )
							ret := 0.238095
					if( d_k > -15.3669 )
						if( rsi1 <= 61.1385 )
							ret := 1.000000 // buy
						if( rsi1 > 61.1385 )
							ret := 0.363636
				if( smoothD_d > 82.6787 )
					if( d_k <= -13.4789 )
						ret := -1.000000 // sell
					if( d_k > -13.4789 )
						if( d_k <= -11.9105 )
							ret := -0.363636
						if( d_k > -11.9105 )
							ret := -0.928571 // sell
			if( d_k > -11.3473 )
				if( d <= 93.8578 )
					if( rsi1 <= 71.4541 )
						if( smoothK_k <= 96.9913 )
							ret := -1.000000 // sell
						if( smoothK_k > 96.9913 )
							ret := 0.190476
					if( rsi1 > 71.4541 )
						if( smoothD_d <= 88.0177 )
							ret := 0.214286
						if( smoothD_d > 88.0177 )
							ret := 0.766667 // buy
				if( d > 93.8578 )
					if( rsi1 <= 83.8523 )
						if( smoothD_d <= 91.7799 )
							ret := -0.695652
						if( smoothD_d > 91.7799 )
							ret := -0.075397
					if( rsi1 > 83.8523 )
						if( rsi1 <= 86.1559 )
							ret := 0.575758
						if( rsi1 > 86.1559 )
							ret := -0.076923
	
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
float op_operation = decision_tree_0_UPST_1Hour_49ffd8ae(rsi1, d, k, smoothD_d, d_k, smoothK_k)

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


