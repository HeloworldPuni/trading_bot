//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: HUBS_30Min_2ST0_9f1ef757 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_HUBS_30Min_2ST0_9f1ef757", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_HUBS_30Min_9f1ef757(d, d_k, smoothK_k, k, rsi1, smoothD_d, ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ema3 <= 287.218 )
		if( ema3 <= 257.249 )
			if( d <= 32.1283 )
				if( rsi1 <= 52.042 )
					if( ema3 <= 42.179 )
						if( k <= 31.1035 )
							ret := 0.537500
						if( k > 31.1035 )
							ret := -0.833333 // sell
					if( ema3 > 42.179 )
						if( ema12 <= -4.21645 )
							ret := -0.597701
						if( ema12 > -4.21645 )
							ret := -0.015408
				if( rsi1 > 52.042 )
					if( k <= 10.0816 )
						if( ema1 <= 120.602 )
							ret := 0.222772
						if( ema1 > 120.602 )
							ret := -0.128713
					if( k > 10.0816 )
						if( d_k <= -6.23626 )
							ret := -0.084079
						if( d_k > -6.23626 )
							ret := -0.379259
			if( d > 32.1283 )
				if( d <= 92.9227 )
					if( ema13 <= 2.13568 )
						if( tema <= 147.675 )
							ret := 0.107401
						if( tema > 147.675 )
							ret := -0.028043
					if( ema13 > 2.13568 )
						if( smoothK_k <= 81.0645 )
							ret := 0.418269
						if( smoothK_k > 81.0645 )
							ret := 0.116923
				if( d > 92.9227 )
					if( ema12 <= 2.94264 )
						if( d_k <= -3.28497 )
							ret := 0.176955
						if( d_k > -3.28497 )
							ret := -0.106256
					if( ema12 > 2.94264 )
						if( tema <= 146.209 )
							ret := 0.882353 // buy
						if( tema > 146.209 )
							ret := 0.083333
		if( ema3 > 257.249 )
			if( tema <= 260.878 )
				if( d_k <= -5.83434 )
					if( rsi1 <= 51.0703 )
						ret := 0.714286 // buy
					if( rsi1 > 51.0703 )
						ret := 0.000000
				if( d_k > -5.83434 )
					if( smoothD_d <= 91.0046 )
						if( ema12 <= -1.51453 )
							ret := 0.953271 // buy
						if( ema12 > -1.51453 )
							ret := 0.703704 // buy
					if( smoothD_d > 91.0046 )
						ret := 0.272727
			if( tema > 260.878 )
				if( smoothK_k <= 61.6464 )
					if( ema13 <= 1.89272 )
						if( d <= 14.5275 )
							ret := 0.396887
						if( d > 14.5275 )
							ret := 0.018059
					if( ema13 > 1.89272 )
						if( d_k <= 12.0209 )
							ret := -0.683099
						if( d_k > 12.0209 )
							ret := 0.043478
				if( smoothK_k > 61.6464 )
					if( d <= 67.8659 )
						if( ema3 <= 285.808 )
							ret := 0.873874 // buy
						if( ema3 > 285.808 )
							ret := -0.181818
					if( d > 67.8659 )
						if( d_k <= -1.09791 )
							ret := -0.025862
						if( d_k > -1.09791 )
							ret := 0.351613
	if( ema3 > 287.218 )
		if( ema1 <= 294.785 )
			if( ema13 <= -2.46023 )
				if( ema13 <= -9.28959 )
					ret := 0.312500
				if( ema13 > -9.28959 )
					if( k <= 0.064084 )
						ret := 0.500000
					if( k > 0.064084 )
						if( k <= 58.1356 )
							ret := -0.489209
						if( k > 58.1356 )
							ret := -0.760331 // sell
			if( ema13 > -2.46023 )
				if( ema2 <= 290.797 )
					if( ema13 <= -0.956153 )
						if( k <= 6.16642 )
							ret := -0.333333
						if( k > 6.16642 )
							ret := 0.745098 // buy
					if( ema13 > -0.956153 )
						if( smoothD_d <= 89.0883 )
							ret := -0.113821
						if( smoothD_d > 89.0883 )
							ret := 0.750000 // buy
				if( ema2 > 290.797 )
					if( d_k <= 5.56948 )
						if( ema3 <= 292.763 )
							ret := -0.411765
						if( ema3 > 292.763 )
							ret := 0.359375
					if( d_k > 5.56948 )
						if( tema <= 294.93 )
							ret := -0.902439 // sell
						if( tema > 294.93 )
							ret := -0.181818
		if( ema1 > 294.785 )
			if( ema3 <= 832.616 )
				if( ema2 <= 752.732 )
					if( ema1 <= 724.095 )
						if( rsi1 <= 81.4928 )
							ret := -0.020754
						if( rsi1 > 81.4928 )
							ret := -0.203938
					if( ema1 > 724.095 )
						if( rsi1 <= 75.6901 )
							ret := -0.800000 // sell
						if( rsi1 > 75.6901 )
							ret := 0.083333
				if( ema2 > 752.732 )
					if( ema1 <= 766.9 )
						if( d <= 14.2722 )
							ret := 0.324324
						if( d > 14.2722 )
							ret := 0.972973 // buy
					if( ema1 > 766.9 )
						if( ema13 <= -4.64844 )
							ret := -0.231884
						if( ema13 > -4.64844 )
							ret := 0.174370
			if( ema3 > 832.616 )
				if( ema3 <= 839.601 )
					if( ema3 <= 834.402 )
						if( rsi1 <= 49.9372 )
							ret := -0.333333
						if( rsi1 > 49.9372 )
							ret := -0.800000 // sell
					if( ema3 > 834.402 )
						if( d_k <= 0.7641 )
							ret := -0.960784 // sell
						if( d_k > 0.7641 )
							ret := -0.608696
				if( ema3 > 839.601 )
					if( k <= 1.60451 )
						ret := -0.636364
					if( k > 1.60451 )
						ret := -0.038462
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_HUBS_30Min_9f1ef757(d, d_k, smoothK_k, k, rsi1, smoothD_d, ema12, ema3, ema13, tema, ema1, ema2)

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


