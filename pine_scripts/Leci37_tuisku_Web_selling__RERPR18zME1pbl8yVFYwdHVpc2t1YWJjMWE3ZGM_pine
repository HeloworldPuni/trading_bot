//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Triple_EMA, L_Vortex_Indicator
// ID_model: DDOG_30Min_2TV0_abc1a7dc Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_DDOG_30Min_2TV0_abc1a7dc", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_DDOG_30Min_abc1a7dc(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6,max_features=sqrt, min_samples_split=10,random_state=843828734)
	if( ema12 <= -0.443925 )
		if( ema1 <= 78.8502 )
			if( ema2 <= 76.9368 )
				if( tema <= 65.3224 )
					if( tema <= 35.7939 )
						if( ema2 <= 34.4368 )
							ret := 0.479167
						if( ema2 > 34.4368 )
							ret := -0.227273
					if( tema > 35.7939 )
						if( ema13 <= -1.1535 )
							ret := 0.338384
						if( ema13 > -1.1535 )
							ret := 0.793103 // buy
				if( tema > 65.3224 )
					if( ema3 <= 76.6027 )
						if( ema3 <= 74.7702 )
							ret := 0.061224
						if( ema3 > 74.7702 )
							ret := 0.698529
					if( ema3 > 76.6027 )
						if( VIP_VIM <= -0.301322 )
							ret := -0.676471
						if( VIP_VIM > -0.301322 )
							ret := 0.363636
			if( ema2 > 76.9368 )
				if( ema2 <= 79.3974 )
					if( ema13 <= -2.22799 )
						if( VIM <= 1.56612 )
							ret := 0.117647
						if( VIM > 1.56612 )
							ret := 1.000000 // buy
					if( ema13 > -2.22799 )
						if( VIM <= 1.35387 )
							ret := 0.663717
						if( VIM > 1.35387 )
							ret := 0.913043 // buy
				if( ema2 > 79.3974 )
					if( tema <= 77.2243 )
						if( ema1 <= 78.6833 )
							ret := -0.166667
						if( ema1 > 78.6833 )
							ret := -1.000000 // sell
					if( tema > 77.2243 )
						if( VIP_VIM <= -0.515303 )
							ret := 1.000000 // buy
						if( VIP_VIM > -0.515303 )
							ret := 0.000000
		if( ema1 > 78.8502 )
			if( ema1 <= 96.7149 )
				if( ema12 <= -1.19696 )
					if( ema1 <= 87.5429 )
						if( ema13 <= -2.82882 )
							ret := 0.785714 // buy
						if( ema13 > -2.82882 )
							ret := 0.523364
					if( ema1 > 87.5429 )
						if( VIP <= 2.02212 )
							ret := 0.111111
						if( VIP > 2.02212 )
							ret := -1.000000 // sell
				if( ema12 > -1.19696 )
					if( VIM <= 1.19664 )
						if( tema <= 95.7662 )
							ret := 0.107417
						if( tema > 95.7662 )
							ret := -1.000000 // sell
					if( VIM > 1.19664 )
						if( ema3 <= 81.0694 )
							ret := -0.631068
						if( ema3 > 81.0694 )
							ret := -0.144022
			if( ema1 > 96.7149 )
				if( ema13 <= -5.21989 )
					if( VIM <= 1.39434 )
						if( ema3 <= 168.703 )
							ret := 0.847826 // buy
						if( ema3 > 168.703 )
							ret := 0.470588
					if( VIM > 1.39434 )
						if( tema <= 152.239 )
							ret := 0.659574
						if( tema > 152.239 )
							ret := -0.423077
				if( ema13 > -5.21989 )
					if( tema <= 139.382 )
						if( ema1 <= 118.237 )
							ret := 0.030933
						if( ema1 > 118.237 )
							ret := 0.198071
					if( tema > 139.382 )
						if( ema12 <= -0.774521 )
							ret := -0.180571
						if( ema12 > -0.774521 )
							ret := 0.240602
	if( ema12 > -0.443925 )
		if( ema3 <= 104.83 )
			if( VIM <= 0.735053 )
				if( ema1 <= 104.491 )
					if( ema3 <= 44.5456 )
						if( ema1 <= 40.7972 )
							ret := -0.048951
						if( ema1 > 40.7972 )
							ret := -0.895833 // sell
					if( ema3 > 44.5456 )
						if( ema1 <= 80.0835 )
							ret := 0.100592
						if( ema1 > 80.0835 )
							ret := -0.178752
				if( ema1 > 104.491 )
					if( ema13 <= 2.41813 )
						if( VIP <= 1.43661 )
							ret := 0.000000
						if( VIP > 1.43661 )
							ret := -1.000000 // sell
					if( ema13 > 2.41813 )
						if( tema <= 108.325 )
							ret := -1.000000 // sell
						if( tema > 108.325 )
							ret := -0.750000 // sell
			if( VIM > 0.735053 )
				if( tema <= 34.6192 )
					if( ema3 <= 34.577 )
						if( ema13 <= -0.291322 )
							ret := -0.202381
						if( ema13 > -0.291322 )
							ret := 0.287582
					if( ema3 > 34.577 )
						if( ema12 <= -0.38923 )
							ret := -0.347826
						if( ema12 > -0.38923 )
							ret := 0.860606 // buy
				if( tema > 34.6192 )
					if( VIM <= 2.21738 )
						if( tema <= 35.0908 )
							ret := -0.466403
						if( tema > 35.0908 )
							ret := 0.018164
					if( VIM > 2.21738 )
						if( tema <= 96.7845 )
							ret := -0.844444 // sell
						if( tema > 96.7845 )
							ret := -0.416667
		if( ema3 > 104.83 )
			if( ema2 <= 105.497 )
				if( VIM <= 1.46433 )
					if( ema13 <= -0.851738 )
						ret := 0.125000
					if( ema13 > -0.851738 )
						if( ema12 <= -0.239026 )
							ret := -0.970588 // sell
						if( ema12 > -0.239026 )
							ret := -0.678161
				if( VIM > 1.46433 )
					ret := 0.833333 // buy
			if( ema2 > 105.497 )
				if( ema12 <= 2.073 )
					if( tema <= 193.343 )
						if( ema2 <= 184.349 )
							ret := -0.090015
						if( ema2 > 184.349 )
							ret := 0.421569
					if( tema > 193.343 )
						if( ema2 <= 193.508 )
							ret := -0.309524
						if( ema2 > 193.508 )
							ret := -0.791045 // sell
				if( ema12 > 2.073 )
					if( ema13 <= 4.95859 )
						if( tema <= 175.431 )
							ret := 0.468182
						if( tema > 175.431 )
							ret := -0.400000
					if( ema13 > 4.95859 )
						if( ema12 <= 4.19526 )
							ret := -0.359551
						if( ema12 > 4.19526 )
							ret := 0.568182
	
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
float op_operation = decision_tree_0_DDOG_30Min_abc1a7dc(ema12, ema3, ema13, tema, ema1, ema2, VIP, VIP_VIM, VIM)

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


