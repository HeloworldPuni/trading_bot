//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA
// ID_model: DBX_1Hour_1T00_fe4b31ca Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DBX_1Hour_1T00_fe4b31ca", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DBX_1Hour_fe4b31ca(ema12, ema3, ema13, tema, ema1, ema2)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ema12 <= 0.022047 )
		if( ema2 <= 20.0017 )
			if( ema1 <= 19.1191 )
				if( tema <= 18.0134 )
					if( ema3 <= 18.0203 )
						if( ema2 <= 16.2934 )
							ret := 0.938776 // buy
						if( ema2 > 16.2934 )
							ret := 0.065934
					if( ema3 > 18.0203 )
						if( ema12 <= -0.357714 )
							ret := -0.444444
						if( ema12 > -0.357714 )
							ret := 0.655022
				if( tema > 18.0134 )
					if( ema13 <= -0.193188 )
						if( ema3 <= 19.1694 )
							ret := 0.712871 // buy
						if( ema3 > 19.1694 )
							ret := -0.292683
					if( ema13 > -0.193188 )
						if( ema3 <= 19.0536 )
							ret := -0.095057
						if( ema3 > 19.0536 )
							ret := -0.546512
			if( ema1 > 19.1191 )
				if( ema1 <= 19.2603 )
					if( ema2 <= 19.211 )
						ret := 0.312500
					if( ema2 > 19.211 )
						if( ema13 <= -0.026149 )
							ret := 0.681481
						if( ema13 > -0.026149 )
							ret := 1.000000 // buy
				if( ema1 > 19.2603 )
					if( ema2 <= 19.7857 )
						if( ema12 <= -0.086653 )
							ret := -0.571429
						if( ema12 > -0.086653 )
							ret := 0.350877
					if( ema2 > 19.7857 )
						if( tema <= 19.8236 )
							ret := 0.689498
						if( tema > 19.8236 )
							ret := 0.223684
		if( ema2 > 20.0017 )
			if( ema13 <= -0.339071 )
				if( tema <= 31.5273 )
					if( ema2 <= 30.5081 )
						if( ema12 <= -0.411445 )
							ret := 0.229787
						if( ema12 > -0.411445 )
							ret := -0.141998
					if( ema2 > 30.5081 )
						if( ema12 <= -0.274862 )
							ret := -0.978261 // sell
						if( ema12 > -0.274862 )
							ret := -0.166667
				if( tema > 31.5273 )
					ret := 0.954545 // buy
			if( ema13 > -0.339071 )
				if( ema12 <= -0.148823 )
					if( tema <= 23.1979 )
						if( tema <= 21.1891 )
							ret := 0.169492
						if( tema > 21.1891 )
							ret := 0.588384
					if( tema > 23.1979 )
						if( tema <= 32.1099 )
							ret := 0.050661
						if( tema > 32.1099 )
							ret := -1.000000 // sell
				if( ema12 > -0.148823 )
					if( ema13 <= -0.29672 )
						if( ema12 <= -0.125041 )
							ret := -0.601770
						if( ema12 > -0.125041 )
							ret := -0.100000
					if( ema13 > -0.29672 )
						if( ema12 <= -0.106144 )
							ret := 0.164251
						if( ema12 > -0.106144 )
							ret := 0.017304
	if( ema12 > 0.022047 )
		if( ema2 <= 22.0589 )
			if( ema2 <= 21.4309 )
				if( ema1 <= 17.2791 )
					if( ema3 <= 15.9083 )
						ret := 0.300000
					if( ema3 > 15.9083 )
						if( ema12 <= 0.053996 )
							ret := -0.120000
						if( ema12 > 0.053996 )
							ret := -0.876190 // sell
				if( ema1 > 17.2791 )
					if( ema13 <= 0.168455 )
						if( tema <= 20.1405 )
							ret := -0.007853
						if( tema > 20.1405 )
							ret := -0.291601
					if( ema13 > 0.168455 )
						if( ema12 <= 0.093069 )
							ret := 0.517483
						if( ema12 > 0.093069 )
							ret := 0.027341
			if( ema2 > 21.4309 )
				if( ema13 <= 0.100305 )
					if( ema12 <= 0.069541 )
						if( tema <= 21.5963 )
							ret := -0.692308
						if( tema > 21.5963 )
							ret := 0.222222
					if( ema12 > 0.069541 )
						if( ema3 <= 21.7542 )
							ret := 0.333333
						if( ema3 > 21.7542 )
							ret := -0.684211
				if( ema13 > 0.100305 )
					if( ema13 <= 1.07364 )
						if( ema12 <= 0.178607 )
							ret := 0.483092
						if( ema12 > 0.178607 )
							ret := 0.186170
					if( ema13 > 1.07364 )
						ret := -1.000000 // sell
		if( ema2 > 22.0589 )
			if( ema13 <= 0.368539 )
				if( ema13 <= 0.107629 )
					if( tema <= 23.6456 )
						if( tema <= 22.9487 )
							ret := -0.180645
						if( tema > 22.9487 )
							ret := -0.617555
					if( tema > 23.6456 )
						if( ema2 <= 23.6755 )
							ret := 0.439394
						if( ema2 > 23.6755 )
							ret := -0.057537
				if( ema13 > 0.107629 )
					if( ema12 <= 0.04562 )
						if( ema2 <= 23.7192 )
							ret := 0.635294
						if( ema2 > 23.7192 )
							ret := 0.235955
					if( ema12 > 0.04562 )
						if( ema1 <= 30.9391 )
							ret := -0.041925
						if( ema1 > 30.9391 )
							ret := -0.413669
			if( ema13 > 0.368539 )
				if( tema <= 27.1078 )
					if( ema13 <= 0.613468 )
						if( ema12 <= 0.231242 )
							ret := -0.508897
						if( ema12 > 0.231242 )
							ret := -0.184358
					if( ema13 > 0.613468 )
						if( ema3 <= 21.9236 )
							ret := -0.291667
						if( ema3 > 21.9236 )
							ret := -0.735632 // sell
				if( tema > 27.1078 )
					if( tema <= 27.9493 )
						if( ema2 <= 27.1937 )
							ret := 0.183673
						if( ema2 > 27.1937 )
							ret := 0.741935 // buy
					if( tema > 27.9493 )
						if( ema12 <= 0.231891 )
							ret := 0.000000
						if( ema12 > 0.231891 )
							ret := -0.370370
	
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
float op_operation = decision_tree_0_DBX_1Hour_fe4b31ca(ema12, ema3, ema13, tema, ema1, ema2)

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


