//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: DOCN_1Hour_1T00_f49825e9 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DOCN_1Hour_1T00_f49825e9", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DOCN_1Hour_f49825e9(ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6,max_features=sqrt, min_samples_split=10,random_state=843828734)
	if( ema13 <= 0.662663 )
		if( tema <= 42.2648 )
			if( ema12 <= 0.187303 )
				if( tema <= 23.0884 )
					if( tema <= 22.1236 )
						if( ema1 <= 20.2474 )
							ret := 0.923077 // buy
						if( ema1 > 20.2474 )
							ret := 0.025641
					if( tema > 22.1236 )
						if( ema2 <= 22.1158 )
							ret := -0.956522 // sell
						if( ema2 > 22.1158 )
							ret := -0.351648
				if( tema > 23.0884 )
					if( ema2 <= 23.8381 )
						if( tema <= 23.2225 )
							ret := 0.181818
						if( tema > 23.2225 )
							ret := 0.823529 // buy
					if( ema2 > 23.8381 )
						if( ema1 <= 23.8545 )
							ret := -0.655172
						if( ema1 > 23.8545 )
							ret := 0.057588
			if( ema12 > 0.187303 )
				if( ema2 <= 23.185 )
					if( tema <= 22.3353 )
						ret := 1.000000 // buy
					if( tema > 22.3353 )
						ret := 0.666667
				if( ema2 > 23.185 )
					if( ema2 <= 38.5814 )
						if( ema12 <= 0.357073 )
							ret := -0.270199
						if( ema12 > 0.357073 )
							ret := 0.050000
					if( ema2 > 38.5814 )
						if( ema1 <= 40.2746 )
							ret := 0.390805
						if( ema1 > 40.2746 )
							ret := -0.053191
		if( tema > 42.2648 )
			if( ema2 <= 45.8167 )
				if( ema1 <= 43.3111 )
					if( ema1 <= 42.7408 )
						if( tema <= 42.32 )
							ret := -0.894737 // sell
						if( tema > 42.32 )
							ret := -0.191781
					if( ema1 > 42.7408 )
						if( ema2 <= 43.46 )
							ret := 0.284091
						if( ema2 > 43.46 )
							ret := -0.666667
				if( ema1 > 43.3111 )
					if( tema <= 44.871 )
						if( ema13 <= 0.613637 )
							ret := -0.503448
						if( ema13 > 0.613637 )
							ret := 0.166667
					if( tema > 44.871 )
						if( ema3 <= 45.2933 )
							ret := -0.583333
						if( ema3 > 45.2933 )
							ret := -0.935484 // sell
			if( ema2 > 45.8167 )
				if( tema <= 47.479 )
					if( ema12 <= -0.667594 )
						if( ema12 <= -1.69775 )
							ret := 0.937500 // buy
						if( ema12 > -1.69775 )
							ret := -0.204301
					if( ema12 > -0.667594 )
						if( tema <= 46.0533 )
							ret := -0.085366
						if( tema > 46.0533 )
							ret := 0.482234
				if( tema > 47.479 )
					if( ema13 <= 0.261003 )
						if( ema2 <= 73.3677 )
							ret := -0.230769
						if( ema2 > 73.3677 )
							ret := 0.053947
					if( ema13 > 0.261003 )
						if( ema13 <= 0.325406 )
							ret := 0.357143
						if( ema13 > 0.325406 )
							ret := 0.042781
	if( ema13 > 0.662663 )
		if( ema13 <= 1.39651 )
			if( ema1 <= 85.3839 )
				if( ema2 <= 63.6813 )
					if( ema2 <= 32.46 )
						if( ema1 <= 28.5094 )
							ret := -0.230769
						if( ema1 > 28.5094 )
							ret := 0.649485
					if( ema2 > 32.46 )
						if( tema <= 33.6943 )
							ret := -0.925926 // sell
						if( tema > 33.6943 )
							ret := 0.162690
				if( ema2 > 63.6813 )
					if( tema <= 82.5248 )
						if( ema13 <= 1.32689 )
							ret := 0.830769 // buy
						if( ema13 > 1.32689 )
							ret := -0.250000
					if( tema > 82.5248 )
						if( ema3 <= 84.1498 )
							ret := -0.473684
						if( ema3 > 84.1498 )
							ret := 0.875000 // buy
			if( ema1 > 85.3839 )
				if( ema12 <= 0.998979 )
					if( ema12 <= 0.472074 )
						if( ema12 <= 0.468038 )
							ret := -0.466667
						if( ema12 > 0.468038 )
							ret := 1.000000 // buy
					if( ema12 > 0.472074 )
						if( ema3 <= 101.204 )
							ret := -0.755556 // sell
						if( ema3 > 101.204 )
							ret := -1.000000 // sell
				if( ema12 > 0.998979 )
					ret := 0.666667
		if( ema13 > 1.39651 )
			if( ema3 <= 106.01 )
				if( ema13 <= 3.09066 )
					if( ema2 <= 90.6716 )
						if( ema1 <= 87.4733 )
							ret := -0.072414
						if( ema1 > 87.4733 )
							ret := 0.789474 // buy
					if( ema2 > 90.6716 )
						if( ema2 <= 92.1764 )
							ret := -0.923077 // sell
						if( ema2 > 92.1764 )
							ret := -0.361702
				if( ema13 > 3.09066 )
					if( ema1 <= 86.0273 )
						if( tema <= 58.2173 )
							ret := 0.230769
						if( tema > 58.2173 )
							ret := -0.743243 // sell
					if( ema1 > 86.0273 )
						if( ema1 <= 100.085 )
							ret := 0.350000
						if( ema1 > 100.085 )
							ret := -0.250000
			if( ema3 > 106.01 )
				if( ema2 <= 114.5 )
					if( ema12 <= 1.58224 )
						if( ema2 <= 114.207 )
							ret := 0.965517 // buy
						if( ema2 > 114.207 )
							ret := 0.750000 // buy
					if( ema12 > 1.58224 )
						if( ema2 <= 109.838 )
							ret := 0.666667
						if( ema2 > 109.838 )
							ret := -0.125000
				if( ema2 > 114.5 )
					if( ema3 <= 120.33 )
						if( ema12 <= 2.53735 )
							ret := -0.882353 // sell
						if( ema12 > 2.53735 )
							ret := 0.000000
					if( ema3 > 120.33 )
						if( ema1 <= 123.373 )
							ret := 0.500000
						if( ema1 > 123.373 )
							ret := -0.055556
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
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
float op_operation = decision_tree_0_DOCN_1Hour_f49825e9(ema12, ema3, ema13, tema, ema1, ema2)

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


