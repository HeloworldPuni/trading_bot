//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: SNAP_1Hour_2TV0_ac4e9e2f Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Hour_2TV0_ac4e9e2f", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Hour_ac4e9e2f(ema1, tema, ema12, ema2, ema3, ema13, VIP_VIM, VIM, VIP)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ema1 <= 11.205 )
		if( VIP_VIM <= 0.319133 )
			if( ema12 <= 0.040588 )
				if( ema3 <= 5.23621 )
					if( ema2 <= 5.06071 )
						ret := 0.714286 // buy
					if( ema2 > 5.06071 )
						if( ema3 <= 5.17344 )
							ret := 1.000000 // buy
						if( ema3 > 5.17344 )
							ret := 0.875000 // buy
				if( ema3 > 5.23621 )
					if( VIM <= 0.857374 )
						if( ema13 <= 0.019126 )
							ret := -0.892857 // sell
						if( ema13 > 0.019126 )
							ret := -0.223684
					if( VIM > 0.857374 )
						if( VIM <= 0.872907 )
							ret := 0.640449
						if( VIM > 0.872907 )
							ret := 0.082002
			if( ema12 > 0.040588 )
				if( VIM <= 0.955466 )
					if( VIP <= 0.978844 )
						ret := -1.000000 // sell
					if( VIP > 0.978844 )
						if( ema2 <= 11.008 )
							ret := -0.067935
						if( ema2 > 11.008 )
							ret := 0.593750
				if( VIM > 0.955466 )
					if( ema2 <= 10.3994 )
						if( ema13 <= 0.093269 )
							ret := -0.410714
						if( ema13 > 0.093269 )
							ret := -0.845528 // sell
					if( ema2 > 10.3994 )
						if( ema3 <= 10.6082 )
							ret := 0.480000
						if( ema3 > 10.6082 )
							ret := -0.417722
		if( VIP_VIM > 0.319133 )
			if( ema1 <= 6.07003 )
				if( VIM <= 0.805 )
					if( VIP <= 1.29812 )
						ret := -0.272727
					if( VIP > 1.29812 )
						ret := 0.833333 // buy
				if( VIM > 0.805 )
					if( tema <= 5.80008 )
						if( ema3 <= 5.10697 )
							ret := -0.692308
						if( ema3 > 5.10697 )
							ret := 0.428571
					if( tema > 5.80008 )
						if( VIP <= 1.26198 )
							ret := -0.550000
						if( VIP > 1.26198 )
							ret := -0.957447 // sell
			if( ema1 > 6.07003 )
				if( tema <= 10.9231 )
					if( ema1 <= 6.242 )
						if( ema2 <= 6.11252 )
							ret := 0.444444
						if( ema2 > 6.11252 )
							ret := 1.000000 // buy
					if( ema1 > 6.242 )
						if( ema3 <= 9.5314 )
							ret := 0.087948
						if( ema3 > 9.5314 )
							ret := 0.415385
				if( tema > 10.9231 )
					if( ema12 <= 0.137517 )
						if( ema1 <= 10.8486 )
							ret := -0.785714 // sell
						if( ema1 > 10.8486 )
							ret := -0.066176
					if( ema12 > 0.137517 )
						if( ema12 <= 0.332606 )
							ret := 0.475000
						if( ema12 > 0.332606 )
							ret := -0.750000 // sell
	if( ema1 > 11.205 )
		if( ema2 <= 12.841 )
			if( ema3 <= 11.205 )
				if( ema12 <= 0.053577 )
					if( tema <= 11.236 )
						ret := -0.250000
					if( tema > 11.236 )
						if( ema1 <= 11.2264 )
							ret := -0.615385
						if( ema1 > 11.2264 )
							ret := -0.941176 // sell
				if( ema12 > 0.053577 )
					if( VIP_VIM <= 0.52192 )
						if( ema1 <= 11.4031 )
							ret := -0.195122
						if( ema1 > 11.4031 )
							ret := 0.684211
					if( VIP_VIM > 0.52192 )
						if( VIM <= 0.654483 )
							ret := -0.886792 // sell
						if( VIM > 0.654483 )
							ret := -0.492754
			if( ema3 > 11.205 )
				if( ema3 <= 11.4924 )
					if( VIM <= 1.16718 )
						if( ema1 <= 11.5042 )
							ret := 0.022523
						if( ema1 > 11.5042 )
							ret := 0.352423
					if( VIM > 1.16718 )
						if( VIP <= 0.874379 )
							ret := -0.019608
						if( VIP > 0.874379 )
							ret := -0.845070 // sell
				if( ema3 > 11.4924 )
					if( ema13 <= -0.015675 )
						if( ema13 <= -0.27997 )
							ret := -0.573684
						if( ema13 > -0.27997 )
							ret := 0.109589
					if( ema13 > -0.015675 )
						if( tema <= 11.7318 )
							ret := -0.801105 // sell
						if( tema > 11.7318 )
							ret := -0.301502
		if( ema2 > 12.841 )
			if( ema2 <= 13.1767 )
				if( VIM <= 1.25382 )
					if( ema3 <= 12.8925 )
						if( ema2 <= 12.9974 )
							ret := 0.000000
						if( ema2 > 12.9974 )
							ret := 0.727273 // buy
					if( ema3 > 12.8925 )
						if( ema3 <= 13.0172 )
							ret := 0.944444 // buy
						if( ema3 > 13.0172 )
							ret := 0.563218
				if( VIM > 1.25382 )
					if( VIP <= 0.770932 )
						ret := 0.666667
					if( VIP > 0.770932 )
						ret := -0.538462
			if( ema2 > 13.1767 )
				if( VIP_VIM <= -0.789773 )
					if( ema2 <= 43.4766 )
						if( ema12 <= -1.26313 )
							ret := -0.142857
						if( ema12 > -1.26313 )
							ret := -0.707071 // sell
					if( ema2 > 43.4766 )
						if( ema3 <= 63.6093 )
							ret := 0.520000
						if( ema3 > 63.6093 )
							ret := -0.703704 // sell
				if( VIP_VIM > -0.789773 )
					if( ema12 <= -0.960496 )
						if( ema13 <= -1.68166 )
							ret := 0.610526
						if( ema13 > -1.68166 )
							ret := -0.258065
					if( ema12 > -0.960496 )
						if( ema3 <= 80.0811 )
							ret := -0.020126
						if( ema3 > 80.0811 )
							ret := -0.979167 // sell
	
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
float op_operation = decision_tree_0_SNAP_1Hour_ac4e9e2f(ema1, tema, ema12, ema2, ema3, ema13, VIP_VIM, VIM, VIP)

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


