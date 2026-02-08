//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: GTLB_30Min_1T00_dbb49693 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_GTLB_30Min_1T00_dbb49693", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_GTLB_30Min_dbb49693(ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( ema3 <= 54.6605 )
		if( ema2 <= 43.4487 )
			if( ema12 <= -0.789286 )
				if( tema <= 37.8339 )
					if( ema12 <= -0.821692 )
						if( tema <= 28.9347 )
							ret := -0.500000
						if( tema > 28.9347 )
							ret := 0.852349 // buy
					if( ema12 > -0.821692 )
						ret := 0.285714
				if( tema > 37.8339 )
					if( ema13 <= -2.26752 )
						if( ema12 <= -1.59448 )
							ret := 0.000000
						if( ema12 > -1.59448 )
							ret := -1.000000 // sell
					if( ema13 > -2.26752 )
						if( ema1 <= 40.8706 )
							ret := -0.250000
						if( ema1 > 40.8706 )
							ret := 0.745098 // buy
			if( ema12 > -0.789286 )
				if( ema2 <= 34.4836 )
					if( ema2 <= 34.2981 )
						if( ema12 <= 0.408149 )
							ret := 0.055308
						if( ema12 > 0.408149 )
							ret := -0.629630
					if( ema2 > 34.2981 )
						if( ema2 <= 34.4385 )
							ret := -0.913043 // sell
						if( ema2 > 34.4385 )
							ret := 0.000000
				if( ema2 > 34.4836 )
					if( tema <= 35.0673 )
						if( tema <= 34.3651 )
							ret := 0.219512
						if( tema > 34.3651 )
							ret := 0.814159 // buy
					if( tema > 35.0673 )
						if( ema13 <= 0.480648 )
							ret := 0.040926
						if( ema13 > 0.480648 )
							ret := 0.274348
		if( ema2 > 43.4487 )
			if( ema2 <= 45.6312 )
				if( ema3 <= 45.3007 )
					if( ema12 <= -0.057408 )
						if( ema12 <= -1.04966 )
							ret := 0.684211
						if( ema12 > -1.04966 )
							ret := -0.271536
					if( ema12 > -0.057408 )
						if( ema13 <= 1.35873 )
							ret := 0.196885
						if( ema13 > 1.35873 )
							ret := -0.443114
				if( ema3 > 45.3007 )
					if( ema1 <= 45.871 )
						if( tema <= 46.0002 )
							ret := -0.573964
						if( tema > 46.0002 )
							ret := 0.400000
					if( ema1 > 45.871 )
						ret := 0.714286 // buy
			if( ema2 > 45.6312 )
				if( ema2 <= 46.3563 )
					if( ema13 <= -1.50637 )
						if( ema12 <= -0.959946 )
							ret := 0.483871
						if( ema12 > -0.959946 )
							ret := -0.656250
					if( ema13 > -1.50637 )
						if( ema2 <= 45.8467 )
							ret := 0.153846
						if( ema2 > 45.8467 )
							ret := 0.600536
				if( ema2 > 46.3563 )
					if( ema3 <= 53.5304 )
						if( ema12 <= -0.475597 )
							ret := 0.140590
						if( ema12 > -0.475597 )
							ret := -0.037681
					if( ema3 > 53.5304 )
						if( tema <= 53.1457 )
							ret := 0.481752
						if( tema > 53.1457 )
							ret := 0.139085
	if( ema3 > 54.6605 )
		if( ema13 <= -1.66211 )
			if( ema12 <= -2.57261 )
				if( ema1 <= 52.2817 )
					ret := 1.000000 // buy
				if( ema1 > 52.2817 )
					if( ema3 <= 77.8154 )
						if( ema13 <= -6.33157 )
							ret := -0.846154 // sell
						if( ema13 > -6.33157 )
							ret := -1.000000 // sell
					if( ema3 > 77.8154 )
						if( ema12 <= -2.72218 )
							ret := -0.136364
						if( ema12 > -2.72218 )
							ret := -1.000000 // sell
			if( ema12 > -2.57261 )
				if( ema12 <= -1.84856 )
					if( ema3 <= 105.278 )
						if( ema1 <= 67.9143 )
							ret := 0.500000
						if( ema1 > 67.9143 )
							ret := 0.933333 // buy
					if( ema3 > 105.278 )
						if( tema <= 104.151 )
							ret := -0.750000 // sell
						if( tema > 104.151 )
							ret := 0.384615
				if( ema12 > -1.84856 )
					if( ema3 <= 121.336 )
						if( ema3 <= 74.7965 )
							ret := 0.194332
						if( ema3 > 74.7965 )
							ret := -0.166008
					if( ema3 > 121.336 )
						ret := 1.000000 // buy
		if( ema13 > -1.66211 )
			if( ema2 <= 55.5865 )
				if( ema12 <= 0.29071 )
					if( ema3 <= 55.3121 )
						if( ema12 <= 0.27621 )
							ret := -0.103774
						if( ema12 > 0.27621 )
							ret := 1.000000 // buy
					if( ema3 > 55.3121 )
						if( ema13 <= -0.343282 )
							ret := -0.704762 // sell
						if( ema13 > -0.343282 )
							ret := -0.326923
				if( ema12 > 0.29071 )
					if( ema3 <= 54.7414 )
						ret := 0.111111
					if( ema3 > 54.7414 )
						if( ema2 <= 55.5499 )
							ret := -0.870588 // sell
						if( ema2 > 55.5499 )
							ret := -0.250000
			if( ema2 > 55.5865 )
				if( ema12 <= 0.780068 )
					if( ema12 <= 0.428652 )
						if( tema <= 57.6372 )
							ret := 0.034571
						if( tema > 57.6372 )
							ret := -0.147118
					if( ema12 > 0.428652 )
						if( ema2 <= 117.872 )
							ret := 0.159732
						if( ema2 > 117.872 )
							ret := -0.806452 // sell
				if( ema12 > 0.780068 )
					if( ema3 <= 60.8639 )
						if( ema3 <= 54.9197 )
							ret := 1.000000 // buy
						if( ema3 > 54.9197 )
							ret := -0.732240 // sell
					if( ema3 > 60.8639 )
						if( ema1 <= 123.461 )
							ret := -0.057940
						if( ema1 > 123.461 )
							ret := -0.803279 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
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
float op_operation = decision_tree_0_GTLB_30Min_dbb49693(ema12, ema3, ema13, tema, ema1, ema2)

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


