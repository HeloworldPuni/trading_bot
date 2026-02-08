//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: BTCUSDT_1Hour_2SV0_0fe3d419 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_BTCUSDT_1Hour_2SV0_0fe3d419", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_BTCUSDT_1Hour_0fe3d419(rsi1, smoothK_k, d_k, k, d, smoothD_d, VIP, VIM, VIP_VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( rsi1 <= 49.9761 )
		if( d_k <= -0.946517 )
			if( VIP <= 0.931379 )
				if( rsi1 <= 40.2046 )
					if( VIP_VIM <= -0.313317 )
						if( rsi1 <= 26.9751 )
							ret := -0.161471
						if( rsi1 > 26.9751 )
							ret := 0.246172
					if( VIP_VIM > -0.313317 )
						if( rsi1 <= 31.0793 )
							ret := -0.604000
						if( rsi1 > 31.0793 )
							ret := -0.123885
				if( rsi1 > 40.2046 )
					if( VIP_VIM <= -0.158672 )
						if( rsi1 <= 43.3932 )
							ret := 0.299046
						if( rsi1 > 43.3932 )
							ret := 0.497180
					if( VIP_VIM > -0.158672 )
						if( d_k <= -19.7642 )
							ret := -0.640000
						if( d_k > -19.7642 )
							ret := 0.041068
			if( VIP > 0.931379 )
				if( smoothK_k <= 9.42926 )
					if( rsi1 <= 41.6607 )
						if( VIM <= 1.06676 )
							ret := -0.756757 // sell
						if( VIM > 1.06676 )
							ret := 0.166667
					if( rsi1 > 41.6607 )
						if( smoothD_d <= 3.39165 )
							ret := 0.209945
						if( smoothD_d > 3.39165 )
							ret := 0.595506
				if( smoothK_k > 9.42926 )
					if( rsi1 <= 41.0685 )
						if( VIM <= 1.04259 )
							ret := -0.794872 // sell
						if( VIM > 1.04259 )
							ret := -0.416667
					if( rsi1 > 41.0685 )
						if( VIP_VIM <= -0.054507 )
							ret := -0.067876
						if( VIP_VIM > -0.054507 )
							ret := -0.333333
		if( d_k > -0.946517 )
			if( rsi1 <= 34.1212 )
				if( VIM <= 1.08072 )
					if( VIM <= 1.00351 )
						if( k <= 4.80461 )
							ret := -0.565789
						if( k > 4.80461 )
							ret := -0.865672 // sell
					if( VIM > 1.00351 )
						if( smoothD_d <= 63.4832 )
							ret := -0.635015
						if( smoothD_d > 63.4832 )
							ret := -0.360000
				if( VIM > 1.08072 )
					if( rsi1 <= 26.6611 )
						if( VIP_VIM <= -0.301697 )
							ret := -0.401079
						if( VIP_VIM > -0.301697 )
							ret := -0.725379 // sell
					if( rsi1 > 26.6611 )
						if( VIP <= 0.852158 )
							ret := -0.080851
						if( VIP > 0.852158 )
							ret := -0.329743
			if( rsi1 > 34.1212 )
				if( VIP_VIM <= 0.019176 )
					if( VIM <= 1.08107 )
						if( d_k <= 2.08252 )
							ret := -0.221591
						if( d_k > 2.08252 )
							ret := -0.068301
					if( VIM > 1.08107 )
						if( d_k <= 11.4139 )
							ret := 0.061117
						if( d_k > 11.4139 )
							ret := 0.333333
				if( VIP_VIM > 0.019176 )
					if( VIM <= 0.922991 )
						if( d_k <= 1.48281 )
							ret := 0.026316
						if( d_k > 1.48281 )
							ret := -0.682432
					if( VIM > 0.922991 )
						if( VIP <= 1.09864 )
							ret := -0.413346
						if( VIP > 1.09864 )
							ret := -0.089928
	if( rsi1 > 49.9761 )
		if( d_k <= 1.23733 )
			if( rsi1 <= 62.361 )
				if( VIP_VIM <= 0.035013 )
					if( VIP_VIM <= -0.083673 )
						if( VIP <= 0.966584 )
							ret := 0.558187
						if( VIP > 0.966584 )
							ret := 0.171123
					if( VIP_VIM > -0.083673 )
						if( rsi1 <= 53.8269 )
							ret := 0.090247
						if( rsi1 > 53.8269 )
							ret := 0.384716
				if( VIP_VIM > 0.035013 )
					if( smoothK_k <= 96.2418 )
						if( VIM <= 0.882065 )
							ret := -0.342048
						if( VIM > 0.882065 )
							ret := -0.014377
					if( smoothK_k > 96.2418 )
						if( rsi1 <= 60.6072 )
							ret := 0.341969
						if( rsi1 > 60.6072 )
							ret := 0.757576 // buy
			if( rsi1 > 62.361 )
				if( VIP <= 1.0848 )
					if( d_k <= -2.91379 )
						if( rsi1 <= 69.7334 )
							ret := 0.579985
						if( rsi1 > 69.7334 )
							ret := 0.781350 // buy
					if( d_k > -2.91379 )
						if( rsi1 <= 63.1864 )
							ret := -0.200000
						if( rsi1 > 63.1864 )
							ret := 0.508734
				if( VIP > 1.0848 )
					if( rsi1 <= 82.3926 )
						if( VIP <= 1.23535 )
							ret := 0.280894
						if( VIP > 1.23535 )
							ret := -0.023983
					if( rsi1 > 82.3926 )
						if( VIP_VIM <= 0.436112 )
							ret := 0.827715 // buy
						if( VIP_VIM > 0.436112 )
							ret := 0.442355
		if( d_k > 1.23733 )
			if( VIP_VIM <= 0.171947 )
				if( rsi1 <= 56.6933 )
					if( VIP_VIM <= 0.013964 )
						if( VIP <= 0.989187 )
							ret := 0.474777
						if( VIP > 0.989187 )
							ret := 0.108392
					if( VIP_VIM > 0.013964 )
						if( d_k <= 24.8056 )
							ret := -0.056951
						if( d_k > 24.8056 )
							ret := 0.782609 // buy
				if( rsi1 > 56.6933 )
					if( rsi1 <= 63.7808 )
						if( smoothD_d <= 36.4009 )
							ret := -0.013453
						if( smoothD_d > 36.4009 )
							ret := 0.314143
					if( rsi1 > 63.7808 )
						if( k <= 82.0484 )
							ret := 0.785714 // buy
						if( k > 82.0484 )
							ret := 0.368421
			if( VIP_VIM > 0.171947 )
				if( rsi1 <= 61.1916 )
					if( VIM <= 0.898203 )
						if( smoothK_k <= 14.4839 )
							ret := -0.089796
						if( smoothK_k > 14.4839 )
							ret := -0.483166
					if( VIM > 0.898203 )
						if( rsi1 <= 53.9795 )
							ret := -0.361446
						if( rsi1 > 53.9795 )
							ret := -0.033748
				if( rsi1 > 61.1916 )
					if( VIP_VIM <= 0.285136 )
						if( k <= 3.23021 )
							ret := -0.648649
						if( k > 3.23021 )
							ret := 0.300422
					if( VIP_VIM > 0.285136 )
						if( rsi1 <= 70.978 )
							ret := -0.160196
						if( rsi1 > 70.978 )
							ret := 0.075550
	
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
float op_operation = decision_tree_0_BTCUSDT_1Hour_0fe3d419(rsi1, smoothK_k, d_k, k, d, smoothD_d, VIP, VIM, VIP_VIM)

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


