//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: AVAXUSDT_30Min_2TV0_405e8818 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AVAXUSDT_30Min_2TV0_405e8818", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AVAXUSDT_30Min_405e8818(ema3, tema, ema2, ema12, ema13, ema1, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=7, max_features=0.82,min_samples_leaf=7, min_samples_split=10,random_state=843828734)
	if( ema12 <= -1.69465 )
		if( ema3 <= 64.7236 )
			if( VIP <= 0.798015 )
				if( ema13 <= -3.40984 )
					if( ema3 <= 63.6466 )
						ret := 1.000000 // buy
					if( ema3 > 63.6466 )
						ret := 0.857143 // buy
				if( ema13 > -3.40984 )
					if( VIP <= 0.739097 )
						if( ema13 <= -3.25235 )
							ret := 0.714286 // buy
						if( ema13 > -3.25235 )
							ret := 1.000000 // buy
					if( VIP > 0.739097 )
						ret := 0.375000
			if( VIP > 0.798015 )
				ret := 0.333333
		if( ema3 > 64.7236 )
			if( tema <= 60.9747 )
				if( ema13 <= -3.79102 )
					ret := -1.000000 // sell
				if( ema13 > -3.79102 )
					ret := -0.857143 // sell
			if( tema > 60.9747 )
				if( VIP <= 0.647544 )
					if( ema13 <= -3.37389 )
						if( tema <= 78.639 )
							ret := -0.285714
						if( tema > 78.639 )
							if( VIP <= 0.597064 )
								ret := 0.363636
							if( VIP > 0.597064 )
								ret := 0.857143 // buy
					if( ema13 > -3.37389 )
						if( VIP <= 0.613844 )
							ret := -0.400000
						if( VIP > 0.613844 )
							ret := -0.857143 // sell
				if( VIP > 0.647544 )
					if( ema1 <= 109.357 )
						if( ema2 <= 105.535 )
							if( ema2 <= 102.131 )
								ret := 0.646465
							if( ema2 > 102.131 )
								ret := 0.142857
						if( ema2 > 105.535 )
							if( tema <= 105.492 )
								ret := 1.000000 // buy
							if( tema > 105.492 )
								ret := 0.857143 // buy
					if( ema1 > 109.357 )
						if( ema1 <= 111.062 )
							ret := -0.428571
						if( ema1 > 111.062 )
							if( ema12 <= -1.78154 )
								ret := 0.789474 // buy
							if( ema12 > -1.78154 )
								ret := 0.000000
	if( ema12 > -1.69465 )
		if( ema3 <= 121.599 )
			if( ema12 <= -0.290621 )
				if( ema3 <= 66.1424 )
					if( ema12 <= -0.921229 )
						if( VIP_VIM <= -0.243 )
							if( VIP_VIM <= -0.65695 )
								ret := -0.163265
							if( VIP_VIM > -0.65695 )
								ret := 0.603774
						if( VIP_VIM > -0.243 )
							if( ema13 <= -2.43259 )
								ret := -1.000000 // sell
							if( ema13 > -2.43259 )
								ret := 0.222222
					if( ema12 > -0.921229 )
						if( ema1 <= 43.5603 )
							if( ema1 <= 41.1535 )
								ret := 0.163127
							if( ema1 > 41.1535 )
								ret := 0.603960
						if( ema1 > 43.5603 )
							if( ema3 <= 51.9733 )
								ret := -0.185921
							if( ema3 > 51.9733 )
								ret := 0.168868
				if( ema3 > 66.1424 )
					if( ema1 <= 64.4972 )
						if( tema <= 63.2347 )
							ret := -0.714286 // sell
						if( tema > 63.2347 )
							ret := -1.000000 // sell
					if( ema1 > 64.4972 )
						if( ema12 <= -1.29947 )
							if( VIP <= 0.856363 )
								ret := 0.352941
							if( VIP > 0.856363 )
								ret := -0.617647
						if( ema12 > -1.29947 )
							if( ema1 <= 93.2732 )
								ret := 0.017249
							if( ema1 > 93.2732 )
								ret := -0.173611
			if( ema12 > -0.290621 )
				if( ema12 <= 2.19234 )
					if( VIP <= 1.15203 )
						if( ema3 <= 29.2738 )
							if( ema13 <= -0.295883 )
								ret := 0.182657
							if( ema13 > -0.295883 )
								ret := 0.038974
						if( ema3 > 29.2738 )
							if( VIM <= 1.13952 )
								ret := -0.002098
							if( VIM > 1.13952 )
								ret := -0.149194
					if( VIP > 1.15203 )
						if( tema <= 6.24679 )
							if( VIM <= 0.768214 )
								ret := -0.250000
							if( VIM > 0.768214 )
								ret := 0.061047
						if( tema > 6.24679 )
							if( ema3 <= 11.5093 )
								ret := 0.251158
							if( ema3 > 11.5093 )
								ret := 0.088022
				if( ema12 > 2.19234 )
					if( ema1 <= 42.0706 )
						ret := 0.454545
					if( ema1 > 42.0706 )
						if( ema13 <= 4.56878 )
							if( ema13 <= 4.25844 )
								ret := -0.644444
							if( ema13 > 4.25844 )
								ret := -0.962963 // sell
						if( ema13 > 4.56878 )
							if( tema <= 114.345 )
								ret := -0.066667
							if( tema > 114.345 )
								ret := -0.777778 // sell
		if( ema3 > 121.599 )
			if( ema12 <= 0.158663 )
				if( ema3 <= 129.777 )
					if( ema2 <= 124.308 )
						if( ema1 <= 123.513 )
							if( VIM <= 1.06508 )
								ret := -0.884615 // sell
							if( VIM > 1.06508 )
								ret := -0.578125
						if( ema1 > 123.513 )
							ret := 0.454545
					if( ema2 > 124.308 )
						if( VIM <= 1.03479 )
							ret := -1.000000 // sell
						if( VIM > 1.03479 )
							if( ema3 <= 128.237 )
								ret := -0.950000 // sell
							if( ema3 > 128.237 )
								ret := -0.555556
				if( ema3 > 129.777 )
					if( ema3 <= 134.25 )
						if( VIM <= 1.09817 )
							if( ema13 <= -1.30554 )
								ret := -0.666667
							if( ema13 > -1.30554 )
								ret := 0.777778 // buy
						if( VIM > 1.09817 )
							if( ema13 <= -2.66959 )
								ret := 0.714286 // buy
							if( ema13 > -2.66959 )
								ret := 1.000000 // buy
					if( ema3 > 134.25 )
						if( ema12 <= -1.29434 )
							ret := -0.142857
						if( ema12 > -1.29434 )
							if( ema1 <= 136.849 )
								ret := -0.820513 // sell
							if( ema1 > 136.849 )
								ret := -0.500000
			if( ema12 > 0.158663 )
				if( ema3 <= 125.245 )
					if( tema <= 125.208 )
						if( VIP <= 1.07279 )
							if( ema13 <= 1.43085 )
								ret := 0.333333
							if( ema13 > 1.43085 )
								ret := 0.916667 // buy
						if( VIP > 1.07279 )
							if( ema13 <= 1.19194 )
								ret := -0.923077 // sell
							if( ema13 > 1.19194 )
								ret := 0.083333
					if( tema > 125.208 )
						if( ema2 <= 124.321 )
							if( ema1 <= 124.631 )
								ret := -1.000000 // sell
							if( ema1 > 124.631 )
								ret := 0.090909
						if( ema2 > 124.321 )
							if( VIP_VIM <= 0.120682 )
								ret := -0.428571
							if( VIP_VIM > 0.120682 )
								ret := -0.875000 // sell
				if( ema3 > 125.245 )
					if( ema1 <= 137.547 )
						if( ema13 <= 0.118373 )
							ret := -0.714286 // sell
						if( ema13 > 0.118373 )
							if( tema <= 138.012 )
								ret := 0.666667
							if( tema > 138.012 )
								ret := -0.428571
					if( ema1 > 137.547 )
						if( tema <= 140.345 )
							ret := -0.909091 // sell
						if( tema > 140.345 )
							ret := -0.333333
	
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
float op_operation = decision_tree_0_AVAXUSDT_30Min_405e8818(ema3, tema, ema2, ema12, ema13, ema1, VIP, VIM, VIP_VIM)

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


