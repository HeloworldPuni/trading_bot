//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: TSLA_1Hour_2SV0_24a1cf51 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_TSLA_1Hour_2SV0_24a1cf51", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_TSLA_1Hour_24a1cf51(rsi1, d, k, smoothD_d, d_k, smoothK_k, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6,max_features=sqrt, min_samples_split=10,random_state=843828734)
	if( k <= 71.5286 )
		if( d_k <= 1.74619 )
			if( rsi1 <= 7.50633 )
				if( VIM <= 1.34438 )
					if( smoothD_d <= -1.20662 )
						if( d <= 0.675679 )
							ret := -0.884615 // sell
						if( d > 0.675679 )
							ret := -0.166667
					if( smoothD_d > -1.20662 )
						if( k <= 5.8333 )
							ret := 0.933333 // buy
						if( k > 5.8333 )
							ret := 0.200000
				if( VIM > 1.34438 )
					if( d_k <= -0.1079 )
						if( VIM <= 12.1784 )
							ret := 0.885057 // buy
						if( VIM > 12.1784 )
							ret := 0.000000
					if( d_k > -0.1079 )
						if( VIP <= 0.607004 )
							ret := -0.147059
						if( VIP > 0.607004 )
							ret := 0.634615
			if( rsi1 > 7.50633 )
				if( smoothK_k <= 26.0825 )
					if( k <= 21.5449 )
						if( smoothK_k <= 16.1778 )
							ret := -0.048068
						if( smoothK_k > 16.1778 )
							ret := 0.125285
					if( k > 21.5449 )
						if( d_k <= -7.50269 )
							ret := -0.067901
						if( d_k > -7.50269 )
							ret := -0.327381
				if( smoothK_k > 26.0825 )
					if( smoothD_d <= 19.0962 )
						if( VIP <= 1.05822 )
							ret := 0.359494
						if( VIP > 1.05822 )
							ret := -0.173469
					if( smoothD_d > 19.0962 )
						if( VIP_VIM <= -0.563878 )
							ret := -0.300000
						if( VIP_VIM > -0.563878 )
							ret := 0.034413
		if( d_k > 1.74619 )
			if( VIP <= 1.19033 )
				if( k <= 0.332635 )
					if( VIP <= 1.00791 )
						if( d_k <= 26.9857 )
							ret := -0.354000
						if( d_k > 26.9857 )
							ret := -0.794872 // sell
					if( VIP > 1.00791 )
						if( d_k <= 4.07124 )
							ret := 0.518519
						if( d_k > 4.07124 )
							ret := -0.207921
				if( k > 0.332635 )
					if( VIM <= 0.841696 )
						if( smoothD_d <= 37.3831 )
							ret := -0.177419
						if( smoothD_d > 37.3831 )
							ret := 0.273438
					if( VIM > 0.841696 )
						if( d <= 24.1612 )
							ret := -0.073612
						if( d > 24.1612 )
							ret := -0.178571
			if( VIP > 1.19033 )
				if( VIM <= 0.851218 )
					if( rsi1 <= 86.4521 )
						if( d <= 66.7598 )
							ret := 0.013675
						if( d > 66.7598 )
							ret := 0.246201
					if( rsi1 > 86.4521 )
						if( smoothD_d <= 62.2653 )
							ret := 0.250000
						if( smoothD_d > 62.2653 )
							ret := -0.750000 // sell
				if( VIM > 0.851218 )
					if( smoothD_d <= 21.5524 )
						if( d_k <= 7.1551 )
							ret := -0.318182
						if( d_k > 7.1551 )
							ret := 0.481481
					if( smoothD_d > 21.5524 )
						if( k <= 60.0072 )
							ret := -0.415323
						if( k > 60.0072 )
							ret := -0.020408
	if( k > 71.5286 )
		if( rsi1 <= 65.2766 )
			if( VIM <= 0.836563 )
				if( k <= 81.8329 )
					if( d <= 88.8955 )
						if( d_k <= 7.80312 )
							ret := -0.571429
						if( d_k > 7.80312 )
							ret := 0.000000
					if( d > 88.8955 )
						if( rsi1 <= 64.4239 )
							ret := -0.952381 // sell
						if( rsi1 > 64.4239 )
							ret := 0.000000
				if( k > 81.8329 )
					if( smoothD_d <= 96.6627 )
						if( VIP <= 1.00087 )
							ret := 0.666667
						if( VIP > 1.00087 )
							ret := -0.100000
					if( smoothD_d > 96.6627 )
						ret := 0.666667
			if( VIM > 0.836563 )
				if( smoothD_d <= 96.349 )
					if( d <= 51.6543 )
						if( k <= 74.489 )
							ret := 0.395349
						if( k > 74.489 )
							ret := 0.720000 // buy
					if( d > 51.6543 )
						if( d_k <= -3.06862 )
							ret := -0.015757
						if( d_k > -3.06862 )
							ret := 0.125124
				if( smoothD_d > 96.349 )
					if( d_k <= -0.428163 )
						if( VIM <= 0.928897 )
							ret := 0.875000 // buy
						if( VIM > 0.928897 )
							ret := -0.250000
					if( d_k > -0.428163 )
						if( k <= 99.8653 )
							ret := -0.673267
						if( k > 99.8653 )
							ret := -0.120482
		if( rsi1 > 65.2766 )
			if( VIP_VIM <= 1.0118 )
				if( VIM <= 0.601612 )
					if( d_k <= 0.452368 )
						if( k <= 98.9576 )
							ret := 0.279070
						if( k > 98.9576 )
							ret := 0.618868
					if( d_k > 0.452368 )
						if( d <= 87.1649 )
							ret := -0.615385
						if( d > 87.1649 )
							ret := 0.237762
				if( VIM > 0.601612 )
					if( smoothD_d <= 81.7012 )
						if( VIP_VIM <= 0.770421 )
							ret := 0.263648
						if( VIP_VIM > 0.770421 )
							ret := -0.758621 // sell
					if( smoothD_d > 81.7012 )
						if( smoothK_k <= 94.5254 )
							ret := 0.073742
						if( smoothK_k > 94.5254 )
							ret := 0.192839
			if( VIP_VIM > 1.0118 )
				if( smoothK_k <= 96.0273 )
					if( k <= 97.3607 )
						if( VIM <= 0.510238 )
							ret := -0.222222
						if( VIM > 0.510238 )
							ret := -1.000000 // sell
					if( k > 97.3607 )
						if( rsi1 <= 94.3854 )
							ret := -0.956522 // sell
						if( rsi1 > 94.3854 )
							ret := -0.750000 // sell
				if( smoothK_k > 96.0273 )
					if( VIM <= 0.471235 )
						if( d_k <= 0.014031 )
							ret := -0.200000
						if( d_k > 0.014031 )
							ret := -1.000000 // sell
					if( VIM > 0.471235 )
						ret := 0.666667
	
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

//CODE associated with the technical indicator L_Vortex_Indicator 
//@version=5
//indicator title = "Vortex Indicator", shorttitle="VI", format=format.price, precision=4, timeframe="", timeframe_gaps=true)
period_ = input.int(14, title="Length", minval=2)
VMP = math.sum( math.abs( high - low[1]), period_ )
VMM = math.sum( math.abs( low - high[1]), period_ )
STR = math.sum( ta.atr(1), period_ )
VIP = VMP / STR
VIM = VMM / STR

VIP_VIM = VIP - VIM

plot(VIP, title="VI +", color=#2962FF)
plot(VIM, title="VI -", color=#E91E63)
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
float op_operation = decision_tree_0_TSLA_1Hour_24a1cf51(rsi1, d, k, smoothD_d, d_k, smoothK_k, VIP, VIP_VIM, VIM)

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


