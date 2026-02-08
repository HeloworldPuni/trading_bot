//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Stochastic_RSI, L_Vortex_Indicator
// ID_model: PTON_1Min_2SV0_829f21ed Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_PTON_1Min_2SV0_829f21ed", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_PTON_1Min_829f21ed(d, d_k, smoothK_k, k, rsi1, smoothD_d, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( rsi1 <= 55.5433 )
		if( VIM <= 1.49097 )
			if( VIM <= 0.999776 )
				if( d_k <= 5.15049 )
					if( d_k <= -27.3397 )
						if( smoothK_k <= 79.107 )
							ret := -0.777778 // sell
						if( smoothK_k > 79.107 )
							ret := 0.066667
					if( d_k > -27.3397 )
						if( d <= 99.1409 )
							ret := 0.207759
						if( d > 99.1409 )
							ret := -0.580645
				if( d_k > 5.15049 )
					if( k <= 0.65222 )
						if( smoothK_k <= -2.97673 )
							ret := -0.236842
						if( smoothK_k > -2.97673 )
							ret := -1.000000 // sell
					if( k > 0.65222 )
						if( k <= 3.99865 )
							ret := 0.551020
						if( k > 3.99865 )
							ret := 0.055990
			if( VIM > 0.999776 )
				if( d_k <= -2.1041 )
					if( d <= 2.74963 )
						if( d_k <= -4.65352 )
							ret := 0.257143
						if( d_k > -4.65352 )
							ret := -0.439024
					if( d > 2.74963 )
						if( rsi1 <= 48.3955 )
							ret := -0.007012
						if( rsi1 > 48.3955 )
							ret := -0.110048
				if( d_k > -2.1041 )
					if( VIP_VIM <= 0.123282 )
						if( d_k <= -0.029094 )
							ret := 0.098901
						if( d_k > -0.029094 )
							ret := 0.022132
					if( VIP_VIM > 0.123282 )
						if( d_k <= 7.76357 )
							ret := 0.011662
						if( d_k > 7.76357 )
							ret := 0.401826
		if( VIM > 1.49097 )
			if( rsi1 <= 45.9104 )
				if( rsi1 <= 37.1241 )
					if( smoothK_k <= 12.4144 )
						if( VIP <= 10.023 )
							ret := 0.373164
						if( VIP > 10.023 )
							ret := -0.413793
					if( smoothK_k > 12.4144 )
						if( smoothD_d <= 53.8961 )
							ret := 0.632458
						if( smoothD_d > 53.8961 )
							ret := 0.229412
				if( rsi1 > 37.1241 )
					if( VIP_VIM <= 0.000204 )
						if( VIM <= 4.60015 )
							ret := 0.184983
						if( VIM > 4.60015 )
							ret := 0.409006
					if( VIP_VIM > 0.000204 )
						if( VIP_VIM <= 0.553069 )
							ret := 0.551724
						if( VIP_VIM > 0.553069 )
							ret := 0.247191
			if( rsi1 > 45.9104 )
				if( d_k <= 0.708046 )
					if( d <= 73.1466 )
						if( smoothK_k <= 18.8374 )
							ret := -0.489231
						if( smoothK_k > 18.8374 )
							ret := -0.167333
					if( d > 73.1466 )
						if( VIP_VIM <= 0.663207 )
							ret := 0.293963
						if( VIP_VIM > 0.663207 )
							ret := -0.333333
				if( d_k > 0.708046 )
					if( rsi1 <= 50.4805 )
						if( VIP_VIM <= 0.014393 )
							ret := 0.158333
						if( VIP_VIM > 0.014393 )
							ret := 0.404255
					if( rsi1 > 50.4805 )
						if( smoothD_d <= 23.7704 )
							ret := -0.446429
						if( smoothD_d > 23.7704 )
							ret := 0.112048
	if( rsi1 > 55.5433 )
		if( VIM <= 1.06335 )
			if( rsi1 <= 72.6916 )
				if( VIP_VIM <= 0.200989 )
					if( rsi1 <= 57.8939 )
						if( VIM <= 0.976174 )
							ret := 0.030108
						if( VIM > 0.976174 )
							ret := -0.163424
					if( rsi1 > 57.8939 )
						if( k <= 92.2134 )
							ret := -0.104440
						if( k > 92.2134 )
							ret := -0.262980
				if( VIP_VIM > 0.200989 )
					if( d <= 45.8678 )
						if( VIP_VIM <= 0.272755 )
							ret := -0.001295
						if( VIP_VIM > 0.272755 )
							ret := -0.225118
					if( d > 45.8678 )
						if( k <= 32.1521 )
							ret := 0.601449
						if( k > 32.1521 )
							ret := 0.020861
			if( rsi1 > 72.6916 )
				if( d_k <= -25.3454 )
					if( d_k <= -31.7816 )
						ret := 0.300000
					if( d_k > -31.7816 )
						if( smoothK_k <= 61.5061 )
							ret := 0.250000
						if( smoothK_k > 61.5061 )
							ret := -0.701754 // sell
				if( d_k > -25.3454 )
					if( VIP <= 1.47427 )
						if( VIP <= 1.31452 )
							ret := -0.157740
						if( VIP > 1.31452 )
							ret := -0.053258
					if( VIP > 1.47427 )
						if( rsi1 <= 85.4985 )
							ret := -0.133333
						if( rsi1 > 85.4985 )
							ret := -0.648649
		if( VIM > 1.06335 )
			if( d_k <= 7.2011 )
				if( d <= 96.7813 )
					if( VIP_VIM <= -3.24717 )
						ret := 0.933333 // buy
					if( VIP_VIM > -3.24717 )
						if( VIP <= 2.7905 )
							ret := -0.292439
						if( VIP > 2.7905 )
							ret := -0.429134
				if( d > 96.7813 )
					if( VIP_VIM <= 0.997512 )
						if( rsi1 <= 56.9017 )
							ret := -0.090909
						if( rsi1 > 56.9017 )
							ret := -0.783626 // sell
					if( VIP_VIM > 0.997512 )
						if( d <= 98.0308 )
							ret := -0.444444
						if( d > 98.0308 )
							ret := 0.166667
			if( d_k > 7.2011 )
				if( smoothK_k <= 46.5855 )
					if( VIP <= 18.7613 )
						if( rsi1 <= 59.1332 )
							ret := -0.116438
						if( rsi1 > 59.1332 )
							ret := -0.522634
					if( VIP > 18.7613 )
						ret := 0.952381 // buy
				if( smoothK_k > 46.5855 )
					if( rsi1 <= 59.8753 )
						if( rsi1 <= 56.1404 )
							ret := 0.666667
						if( rsi1 > 56.1404 )
							ret := -0.244094
					if( rsi1 > 59.8753 )
						if( d_k <= 15.5029 )
							ret := 0.565737
						if( d_k > 15.5029 )
							ret := -0.222222
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
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
float op_operation = decision_tree_0_PTON_1Min_829f21ed(d, d_k, smoothK_k, k, rsi1, smoothD_d, VIP, VIP_VIM, VIM)

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


