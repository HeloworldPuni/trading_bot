//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: DBX_30Min_2TV0_02682431 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DBX_30Min_2TV0_02682431", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DBX_30Min_02682431(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( ema12 <= -0.015941 )
		if( VIP <= 1.33955 )
			if( ema3 <= 31.7522 )
				if( tema <= 16.1041 )
					if( VIM <= 1.37831 )
						if( VIP <= 0.801512 )
							ret := 0.250000
						if( VIP > 0.801512 )
							ret := 0.950000 // buy
					if( VIM > 1.37831 )
						ret := -0.500000
				if( tema > 16.1041 )
					if( ema12 <= -0.790344 )
						if( VIP <= 0.499521 )
							ret := 0.000000
						if( VIP > 0.499521 )
							ret := -1.000000 // sell
					if( ema12 > -0.790344 )
						if( ema3 <= 31.462 )
							ret := 0.067711
						if( ema3 > 31.462 )
							ret := 0.556150
			if( ema3 > 31.7522 )
				if( ema2 <= 31.8863 )
					if( VIM <= 1.4168 )
						if( ema12 <= -0.109903 )
							ret := -0.616667
						if( ema12 > -0.109903 )
							ret := -0.938776 // sell
					if( VIM > 1.4168 )
						if( VIM <= 1.43382 )
							ret := 1.000000 // buy
						if( VIM > 1.43382 )
							ret := 0.100000
				if( ema2 > 31.8863 )
					if( ema13 <= 0.00227 )
						if( ema3 <= 32.3501 )
							ret := 0.214286
						if( ema3 > 32.3501 )
							ret := -0.341651
					if( ema13 > 0.00227 )
						if( tema <= 32.0999 )
							ret := -1.000000 // sell
						if( tema > 32.0999 )
							ret := 0.692308
		if( VIP > 1.33955 )
			if( VIM <= 1.09578 )
				if( ema2 <= 21.8879 )
					ret := -1.000000 // sell
				if( ema2 > 21.8879 )
					if( VIP <= 1.45481 )
						if( VIP_VIM <= 0.491159 )
							ret := 0.187500
						if( VIP_VIM > 0.491159 )
							ret := 1.000000 // buy
					if( VIP > 1.45481 )
						if( ema2 <= 24.8052 )
							ret := -0.045455
						if( ema2 > 24.8052 )
							ret := -1.000000 // sell
			if( VIM > 1.09578 )
				if( VIP_VIM <= 0.109754 )
					if( VIP <= 1.9609 )
						if( ema13 <= -0.528972 )
							ret := 0.947368 // buy
						if( ema13 > -0.528972 )
							ret := 0.296791
					if( VIP > 1.9609 )
						if( VIP_VIM <= 0.037327 )
							ret := 0.141304
						if( VIP_VIM > 0.037327 )
							ret := -0.730769 // sell
				if( VIP_VIM > 0.109754 )
					if( ema13 <= -0.055082 )
						if( ema13 <= -0.341031 )
							ret := -0.666667
						if( ema13 > -0.341031 )
							ret := 0.301170
					if( ema13 > -0.055082 )
						if( ema2 <= 21.684 )
							ret := 0.984615 // buy
						if( ema2 > 21.684 )
							ret := 0.640000
	if( ema12 > -0.015941 )
		if( ema2 <= 22.2045 )
			if( ema12 <= 0.029492 )
				if( VIP_VIM <= -0.180179 )
					if( VIP <= 1.29251 )
						if( ema12 <= -0.012485 )
							ret := -0.545455
						if( ema12 > -0.012485 )
							ret := -0.153846
					if( VIP > 1.29251 )
						if( ema3 <= 20.4932 )
							ret := -0.125000
						if( ema3 > 20.4932 )
							ret := 0.804878 // buy
				if( VIP_VIM > -0.180179 )
					if( ema3 <= 18.0917 )
						if( ema3 <= 17.927 )
							ret := 0.267857
						if( ema3 > 17.927 )
							ret := 0.798319 // buy
					if( ema3 > 18.0917 )
						if( ema3 <= 18.6033 )
							ret := -0.115789
						if( ema3 > 18.6033 )
							ret := 0.167932
			if( ema12 > 0.029492 )
				if( tema <= 22.0531 )
					if( tema <= 16.342 )
						if( VIM <= 0.939561 )
							ret := -1.000000 // sell
						if( VIM > 0.939561 )
							ret := 1.000000 // buy
					if( tema > 16.342 )
						if( ema2 <= 19.711 )
							ret := -0.213182
						if( ema2 > 19.711 )
							ret := -0.048447
				if( tema > 22.0531 )
					if( ema13 <= 0.275 )
						if( ema12 <= 0.152992 )
							ret := 0.056838
						if( ema12 > 0.152992 )
							ret := -0.466667
					if( ema13 > 0.275 )
						if( VIM <= 0.891475 )
							ret := 0.260870
						if( VIM > 0.891475 )
							ret := 0.762238 // buy
		if( ema2 > 22.2045 )
			if( ema2 <= 25.4457 )
				if( VIM <= 1.25548 )
					if( tema <= 25.5597 )
						if( ema12 <= 0.100693 )
							ret := -0.080417
						if( ema12 > 0.100693 )
							ret := -0.206597
					if( tema > 25.5597 )
						if( VIM <= 0.904882 )
							ret := -0.878378 // sell
						if( VIM > 0.904882 )
							ret := -0.357143
				if( VIM > 1.25548 )
					if( ema2 <= 24.8235 )
						if( ema2 <= 22.3958 )
							ret := -0.835821 // sell
						if( ema2 > 22.3958 )
							ret := -0.223186
					if( ema2 > 24.8235 )
						if( VIP_VIM <= -0.005377 )
							ret := -0.863636 // sell
						if( VIP_VIM > -0.005377 )
							ret := -0.470588
			if( ema2 > 25.4457 )
				if( ema2 <= 31.6724 )
					if( ema2 <= 31.4144 )
						if( ema1 <= 31.2358 )
							ret := 0.017556
						if( ema1 > 31.2358 )
							ret := -0.422642
					if( ema2 > 31.4144 )
						if( ema13 <= 0.169667 )
							ret := 0.148649
						if( ema13 > 0.169667 )
							ret := 0.609929
				if( ema2 > 31.6724 )
					if( ema13 <= 0.640818 )
						if( ema13 <= 0.295132 )
							ret := -0.243863
						if( ema13 > 0.295132 )
							ret := -0.600000
					if( ema13 > 0.640818 )
						if( tema <= 42.4191 )
							ret := 0.282759
						if( tema > 42.4191 )
							ret := -1.000000 // sell
	
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
float op_operation = decision_tree_0_DBX_30Min_02682431(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)

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


