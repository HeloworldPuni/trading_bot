//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Triple_EMA
// ID_model: RUN_5Min_2ST0_f3964dcb Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_RUN_5Min_2ST0_f3964dcb", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_RUN_5Min_f3964dcb(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ema1 <= 9.44045 )
		if( d_k <= -0.880009 )
			if( rsi1 <= 55.0693 )
				if( ema12 <= -0.118573 )
					ret := -0.157895
				if( ema12 > -0.118573 )
					if( ema12 <= -0.046662 )
						if( d_k <= -5.84397 )
							ret := 0.953125 // buy
						if( d_k > -5.84397 )
							ret := 0.650000
					if( ema12 > -0.046662 )
						if( ema12 <= -0.018196 )
							ret := 0.259259
						if( ema12 > -0.018196 )
							ret := 0.734848 // buy
			if( rsi1 > 55.0693 )
				if( ema3 <= 9.24526 )
					if( ema3 <= 9.01934 )
						if( smoothD_d <= 93.3591 )
							ret := -0.500000
						if( smoothD_d > 93.3591 )
							ret := 0.769231 // buy
					if( ema3 > 9.01934 )
						if( d <= 69.7369 )
							ret := 1.000000 // buy
						if( d > 69.7369 )
							ret := 0.529412
				if( ema3 > 9.24526 )
					if( rsi1 <= 72.3125 )
						if( ema13 <= -0.005624 )
							ret := -0.500000
						if( ema13 > -0.005624 )
							ret := 0.150000
					if( rsi1 > 72.3125 )
						ret := -0.714286 // sell
		if( d_k > -0.880009 )
			if( smoothD_d <= 70.956 )
				if( k <= 48.3263 )
					if( ema12 <= -0.043456 )
						if( smoothD_d <= 10.3351 )
							ret := 0.117647
						if( smoothD_d > 10.3351 )
							ret := 0.794872 // buy
					if( ema12 > -0.043456 )
						if( ema12 <= -0.015952 )
							ret := -0.393443
						if( ema12 > -0.015952 )
							ret := 0.101124
				if( k > 48.3263 )
					if( ema2 <= 8.93209 )
						ret := 0.333333
					if( ema2 > 8.93209 )
						if( rsi1 <= 50.2632 )
							ret := 0.684211
						if( rsi1 > 50.2632 )
							ret := 0.967742 // buy
			if( smoothD_d > 70.956 )
				if( tema <= 9.22296 )
					if( tema <= 8.94188 )
						if( rsi1 <= 53.7088 )
							ret := -0.352941
						if( rsi1 > 53.7088 )
							ret := 0.684211
					if( tema > 8.94188 )
						if( d_k <= 0.734684 )
							ret := -0.807018 // sell
						if( d_k > 0.734684 )
							ret := -0.354839
				if( tema > 9.22296 )
					if( d_k <= 0.16925 )
						ret := 0.950000 // buy
					if( d_k > 0.16925 )
						if( ema13 <= 0.01943 )
							ret := 0.444444
						if( ema13 > 0.01943 )
							ret := -0.200000
	if( ema1 > 9.44045 )
		if( rsi1 <= 76.142 )
			if( d_k <= -2.24913 )
				if( k <= 36.6715 )
					if( ema1 <= 12.8642 )
						if( ema3 <= 12.1089 )
							ret := -0.001832
						if( ema3 > 12.1089 )
							ret := -0.310719
					if( ema1 > 12.8642 )
						if( tema <= 14.5445 )
							ret := 0.248993
						if( tema > 14.5445 )
							ret := 0.054389
				if( k > 36.6715 )
					if( tema <= 18.8699 )
						if( ema2 <= 17.5995 )
							ret := -0.055863
						if( ema2 > 17.5995 )
							ret := 0.075558
					if( tema > 18.8699 )
						if( smoothD_d <= 45.2804 )
							ret := -0.268403
						if( smoothD_d > 45.2804 )
							ret := -0.109170
			if( d_k > -2.24913 )
				if( ema3 <= 11.8718 )
					if( ema12 <= 0.088941 )
						if( smoothK_k <= 96.8555 )
							ret := 0.069681
						if( smoothK_k > 96.8555 )
							ret := 0.495050
					if( ema12 > 0.088941 )
						if( ema1 <= 10.6228 )
							ret := -0.150685
						if( ema1 > 10.6228 )
							ret := 0.677419
				if( ema3 > 11.8718 )
					if( smoothD_d <= -2.66926 )
						if( ema1 <= 18.8932 )
							ret := -0.024664
						if( ema1 > 18.8932 )
							ret := -0.576923
					if( smoothD_d > -2.66926 )
						if( d <= 4.52795 )
							ret := 0.119869
						if( d > 4.52795 )
							ret := 0.003127
		if( rsi1 > 76.142 )
			if( d <= 99.0539 )
				if( ema3 <= 16.326 )
					if( ema13 <= 0.266915 )
						if( smoothD_d <= 49.9927 )
							ret := -0.528000
						if( smoothD_d > 49.9927 )
							ret := -0.145174
					if( ema13 > 0.266915 )
						if( k <= 52.979 )
							ret := -0.553191
						if( k > 52.979 )
							ret := 0.284065
				if( ema3 > 16.326 )
					if( d <= 97.5552 )
						if( ema12 <= 0.200936 )
							ret := -0.150485
						if( ema12 > 0.200936 )
							ret := -0.652439
					if( d > 97.5552 )
						if( ema12 <= 0.142203 )
							ret := -0.492188
						if( ema12 > 0.142203 )
							ret := -0.936170 // sell
			if( d > 99.0539 )
				if( ema3 <= 14.216 )
					if( ema3 <= 11.9753 )
						if( ema13 <= 0.119902 )
							ret := 0.648649
						if( ema13 > 0.119902 )
							ret := -0.294872
					if( ema3 > 11.9753 )
						if( rsi1 <= 81.2711 )
							ret := -0.162162
						if( rsi1 > 81.2711 )
							ret := 0.790055 // buy
				if( ema3 > 14.216 )
					if( d_k <= -0.015236 )
						if( ema13 <= 0.278584 )
							ret := -0.350000
						if( ema13 > 0.278584 )
							ret := -0.944444 // sell
					if( d_k > -0.015236 )
						if( rsi1 <= 92.3257 )
							ret := -0.008850
						if( rsi1 > 92.3257 )
							ret := 0.823529 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 5Min pine_value: 5   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  5MIN !!"
if (str.tostring(timeframe.period) != "5")
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
float op_operation = decision_tree_0_RUN_5Min_f3964dcb(d_k, d, rsi1, k, smoothD_d, smoothK_k, ema1, tema, ema12, ema2, ema3, ema13)

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


