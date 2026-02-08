//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI
// ID_model: QCOM_1Hour_1S00_e1025a9e Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_QCOM_1Hour_1S00_e1025a9e", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_QCOM_1Hour_e1025a9e(rsi1, d, k, smoothD_d, d_k, smoothK_k)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( k <= 20.3436 )
		if( rsi1 <= 24.5302 )
			if( d <= 9.10344 )
				if( d_k <= -0.030466 )
					if( smoothK_k <= -2.13684 )
						if( rsi1 <= 23.1834 )
							ret := 0.702381 // buy
						if( rsi1 > 23.1834 )
							ret := -0.333333
					if( smoothK_k > -2.13684 )
						if( smoothD_d <= -0.31136 )
							ret := -0.134615
						if( smoothD_d > -0.31136 )
							ret := 0.205056
				if( d_k > -0.030466 )
					if( d <= 5.19029 )
						if( k <= 1.78517 )
							ret := -0.082105
						if( k > 1.78517 )
							ret := 0.297710
					if( d > 5.19029 )
						if( rsi1 <= 20.0473 )
							ret := -0.671875
						if( rsi1 > 20.0473 )
							ret := 0.000000
			if( d > 9.10344 )
				if( smoothK_k <= 10.9005 )
					if( d_k <= 1.28782 )
						if( smoothK_k <= 10.5873 )
							ret := 0.862745 // buy
						if( smoothK_k > 10.5873 )
							ret := 0.375000
					if( d_k > 1.28782 )
						if( smoothK_k <= 1.01148 )
							ret := 0.600000
						if( smoothK_k > 1.01148 )
							ret := 0.181818
				if( smoothK_k > 10.9005 )
					if( smoothK_k <= 16.3735 )
						if( smoothD_d <= 7.96929 )
							ret := 0.619048
						if( smoothD_d > 7.96929 )
							ret := -0.202899
					if( smoothK_k > 16.3735 )
						if( rsi1 <= 23.2126 )
							ret := 0.178571
						if( rsi1 > 23.2126 )
							ret := 0.882353 // buy
		if( rsi1 > 24.5302 )
			if( rsi1 <= 64.0644 )
				if( smoothD_d <= 45.2345 )
					if( k <= 20.2249 )
						if( d_k <= 19.2211 )
							ret := -0.089382
						if( d_k > 19.2211 )
							ret := 0.079365
					if( k > 20.2249 )
						if( d_k <= -10.7497 )
							ret := 1.000000 // buy
						if( d_k > -10.7497 )
							ret := -0.766667 // sell
				if( smoothD_d > 45.2345 )
					if( k <= 20.2339 )
						ret := -1.000000 // sell
					if( k > 20.2339 )
						ret := 0.000000
			if( rsi1 > 64.0644 )
				if( smoothD_d <= 8.93729 )
					if( d <= 5.32214 )
						if( d_k <= 0.938777 )
							ret := 0.071429
						if( d_k > 0.938777 )
							ret := -0.555556
					if( d > 5.32214 )
						if( smoothK_k <= 8.39015 )
							ret := -0.913793 // sell
						if( smoothK_k > 8.39015 )
							ret := -0.555556
				if( smoothD_d > 8.93729 )
					if( smoothD_d <= 15.5601 )
						if( rsi1 <= 71.5903 )
							ret := 0.583333
						if( rsi1 > 71.5903 )
							ret := -0.272727
					if( smoothD_d > 15.5601 )
						if( smoothD_d <= 29.9988 )
							ret := -0.521739
						if( smoothD_d > 29.9988 )
							ret := -0.083333
	if( k > 20.3436 )
		if( d_k <= -5.36554 )
			if( rsi1 <= 67.7046 )
				if( d_k <= -29.1425 )
					if( d <= 65.2816 )
						if( smoothD_d <= 49.654 )
							ret := 0.400000
						if( smoothD_d > 49.654 )
							ret := 0.852459 // buy
					if( d > 65.2816 )
						if( smoothK_k <= 96.8158 )
							ret := -0.714286 // sell
						if( smoothK_k > 96.8158 )
							ret := 0.250000
				if( d_k > -29.1425 )
					if( smoothK_k <= 24.3462 )
						if( d_k <= -13.2357 )
							ret := 0.735849 // buy
						if( d_k > -13.2357 )
							ret := 0.269474
					if( smoothK_k > 24.3462 )
						if( rsi1 <= 39.2313 )
							ret := -0.031490
						if( rsi1 > 39.2313 )
							ret := 0.107265
			if( rsi1 > 67.7046 )
				if( rsi1 <= 89.8726 )
					if( k <= 53.8574 )
						if( d_k <= -14.7565 )
							ret := -0.153846
						if( d_k > -14.7565 )
							ret := -0.565217
					if( k > 53.8574 )
						if( d_k <= -8.26472 )
							ret := -0.122830
						if( d_k > -8.26472 )
							ret := 0.139918
				if( rsi1 > 89.8726 )
					if( rsi1 <= 93.3517 )
						if( k <= 99.9426 )
							ret := 0.913043 // buy
						if( k > 99.9426 )
							ret := -1.000000 // sell
					if( rsi1 > 93.3517 )
						ret := -0.235294
		if( d_k > -5.36554 )
			if( k <= 20.4416 )
				if( k <= 20.3596 )
					ret := 0.444444
				if( k > 20.3596 )
					if( smoothK_k <= 17.419 )
						ret := 1.000000 // buy
					if( smoothK_k > 17.419 )
						ret := 0.666667
			if( k > 20.4416 )
				if( d_k <= 0.370779 )
					if( d <= 21.9949 )
						if( smoothK_k <= 20.1836 )
							ret := -0.014851
						if( smoothK_k > 20.1836 )
							ret := 0.521368
					if( d > 21.9949 )
						if( smoothK_k <= 78.4423 )
							ret := -0.168182
						if( smoothK_k > 78.4423 )
							ret := -0.034051
				if( d_k > 0.370779 )
					if( rsi1 <= 81.8213 )
						if( rsi1 <= 50.997 )
							ret := 0.057884
						if( rsi1 > 50.997 )
							ret := -0.030984
					if( rsi1 > 81.8213 )
						if( smoothK_k <= 85.6295 )
							ret := 0.600000
						if( smoothK_k > 85.6295 )
							ret := -0.083682
	
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
float op_operation = decision_tree_0_QCOM_1Hour_e1025a9e(rsi1, d, k, smoothD_d, d_k, smoothK_k)

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


