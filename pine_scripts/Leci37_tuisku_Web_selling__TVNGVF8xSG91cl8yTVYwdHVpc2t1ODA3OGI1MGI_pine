//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Vortex_Indicator
// ID_model: MSFT_1Hour_2MV0_8078b50b Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_MSFT_1Hour_2MV0_8078b50b", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_MSFT_1Hour_8078b50b(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, VIP, VIP_VIM, VIM)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=6, max_features=0.7, min_samples_split=10,random_state=843828734)
	if( Positive_Money_Flow_Sum <= 2.86514e+09 )
		if( Typical_Price <= 104.872 )
			if( VIM <= 1.35745 )
				if( MFI <= 46.6937 )
					if( VIP_VIM <= -0.294954 )
						if( Typical_Price <= 97.7152 )
							ret := 1.000000 // buy
						if( Typical_Price > 97.7152 )
							ret := 0.103448
					if( VIP_VIM > -0.294954 )
						if( Negative_Money_Flow_Sum <= 1.97434e+09 )
							ret := 0.389831
						if( Negative_Money_Flow_Sum > 1.97434e+09 )
							ret := 0.880000 // buy
				if( MFI > 46.6937 )
					if( VIP <= 1.15707 )
						if( Negative_Money_Flow <= 1.04593e+08 )
							ret := -0.290323
						if( Negative_Money_Flow > 1.04593e+08 )
							ret := 0.529412
					if( VIP > 1.15707 )
						if( MFI_Low <= 43.1042 )
							ret := 0.142857
						if( MFI_Low > 43.1042 )
							ret := 0.750000 // buy
			if( VIM > 1.35745 )
				ret := -1.000000 // sell
		if( Typical_Price > 104.872 )
			if( Raw_Money_Flow <= 867926 )
				if( Negative_Money_Flow_Sum <= 2.33694e+09 )
					if( Negative_Money_Flow_Sum <= 2.31367e+09 )
						if( Money_Flow_Ratio <= 0.756931 )
							ret := 0.172185
						if( Money_Flow_Ratio > 0.756931 )
							ret := -0.263889
					if( Negative_Money_Flow_Sum > 2.31367e+09 )
						if( MFI <= 39.9304 )
							ret := -0.977778 // sell
						if( MFI > 39.9304 )
							ret := -0.375000
				if( Negative_Money_Flow_Sum > 2.33694e+09 )
					if( VIP_VIM <= -0.449922 )
						if( VIP <= 0.78188 )
							ret := -0.033333
						if( VIP > 0.78188 )
							ret := -0.694444
					if( VIP_VIM > -0.449922 )
						if( VIP <= 0.793615 )
							ret := 0.818182 // buy
						if( VIP > 0.793615 )
							ret := 0.112128
			if( Raw_Money_Flow > 867926 )
				if( Negative_Money_Flow_Sum <= 9.53195e+09 )
					if( VIM <= 1.19339 )
						if( Positive_Money_Flow <= 7.41507e+08 )
							ret := 0.091902
						if( Positive_Money_Flow > 7.41507e+08 )
							ret := -0.115479
					if( VIM > 1.19339 )
						if( Negative_Money_Flow_Sum <= 6.57025e+09 )
							ret := -0.098592
						if( Negative_Money_Flow_Sum > 6.57025e+09 )
							ret := 0.104637
				if( Negative_Money_Flow_Sum > 9.53195e+09 )
					if( Negative_Money_Flow <= 1.7427e+07 )
						if( VIP <= 0.887095 )
							ret := -0.008929
						if( VIP > 0.887095 )
							ret := 0.622222
					if( Negative_Money_Flow > 1.7427e+07 )
						if( Negative_Money_Flow <= 2.5575e+09 )
							ret := 0.692308
						if( Negative_Money_Flow > 2.5575e+09 )
							ret := -0.071429
	if( Positive_Money_Flow_Sum > 2.86514e+09 )
		if( VIP <= 0.926729 )
			if( Negative_Money_Flow_Sum <= 7.00911e+09 )
				if( Typical_Price <= 256.006 )
					if( MFI <= 62.877 )
						if( MFI_Low <= 29.1123 )
							ret := 0.110092
						if( MFI_Low > 29.1123 )
							ret := -0.253968
					if( MFI > 62.877 )
						if( Typical_Price <= 243.195 )
							ret := 0.600000
						if( Typical_Price > 243.195 )
							ret := -0.173913
				if( Typical_Price > 256.006 )
					if( Negative_Money_Flow_Sum <= 6.93251e+09 )
						if( Negative_Money_Flow <= 1.07033e+09 )
							ret := -0.301370
						if( Negative_Money_Flow > 1.07033e+09 )
							ret := 0.040984
					if( Negative_Money_Flow_Sum > 6.93251e+09 )
						if( Money_Flow_Ratio <= 0.771697 )
							ret := 1.000000 // buy
						if( Money_Flow_Ratio > 0.771697 )
							ret := -1.000000 // sell
			if( Negative_Money_Flow_Sum > 7.00911e+09 )
				if( Negative_Money_Flow_Sum <= 1.48075e+10 )
					if( Positive_Money_Flow_Sum <= 3.05665e+09 )
						if( Typical_Price <= 361.224 )
							ret := -0.929688 // sell
						if( Typical_Price > 361.224 )
							ret := 0.388889
					if( Positive_Money_Flow_Sum > 3.05665e+09 )
						if( Negative_Money_Flow <= 8.7408e+08 )
							ret := -0.246063
						if( Negative_Money_Flow > 8.7408e+08 )
							ret := -0.671875
				if( Negative_Money_Flow_Sum > 1.48075e+10 )
					if( VIM <= 1.22769 )
						if( Typical_Price <= 273.109 )
							ret := -0.500000
						if( Typical_Price > 273.109 )
							ret := 1.000000 // buy
					if( VIM > 1.22769 )
						ret := -0.400000
		if( VIP > 0.926729 )
			if( MFI_High <= -28.7218 )
				if( VIP_VIM <= -0.114158 )
					if( VIM <= 1.15455 )
						if( Money_Flow_Ratio <= 0.944162 )
							ret := -0.522449
						if( Money_Flow_Ratio > 0.944162 )
							ret := -0.114754
					if( VIM > 1.15455 )
						if( Negative_Money_Flow_Sum <= 8.33964e+09 )
							ret := -0.006135
						if( Negative_Money_Flow_Sum > 8.33964e+09 )
							ret := 0.734694 // buy
				if( VIP_VIM > -0.114158 )
					if( Money_Flow_Ratio <= 0.688389 )
						if( Negative_Money_Flow_Sum <= 7.54996e+09 )
							ret := -0.225225
						if( Negative_Money_Flow_Sum > 7.54996e+09 )
							ret := 0.333333
					if( Money_Flow_Ratio > 0.688389 )
						if( Typical_Price <= 297.458 )
							ret := 0.367969
						if( Typical_Price > 297.458 )
							ret := 0.077465
			if( MFI_High > -28.7218 )
				if( Money_Flow_Ratio <= 1.1758 )
					if( MFI <= 53.4897 )
						if( VIP_VIM <= 0.204365 )
							ret := -0.018828
						if( VIP_VIM > 0.204365 )
							ret := -0.435754
					if( MFI > 53.4897 )
						if( Negative_Money_Flow <= 6.17544e+08 )
							ret := -0.726744 // sell
						if( Negative_Money_Flow > 6.17544e+08 )
							ret := 0.000000
				if( Money_Flow_Ratio > 1.1758 )
					if( Negative_Money_Flow_Sum <= 4.77608e+09 )
						if( Negative_Money_Flow <= 9.65406e+08 )
							ret := -0.030336
						if( Negative_Money_Flow > 9.65406e+08 )
							ret := 0.186992
					if( Negative_Money_Flow_Sum > 4.77608e+09 )
						if( VIP_VIM <= 0.150611 )
							ret := 0.063492
						if( VIP_VIM > 0.150611 )
							ret := -0.608163
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Money_Flow_Index 
//@version=5
//indicator title="Money Flow Index (MFI)", shorttitle="MFI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)

// Input parameters
length_MFI = input.int(14, minval=1, title="MFI Length")

// Calculate the Typical Price
Typical_Price = (high + low + close) / 3

// Calculate Raw Money Flow
Raw_Money_Flow = Typical_Price * volume

// Calculate Positive and Negative Money Flow
Positive_Money_Flow = Raw_Money_Flow * (Typical_Price > Typical_Price[1] ? 1 : 0)
Negative_Money_Flow = Raw_Money_Flow * (Typical_Price < Typical_Price[1] ? 1 : 0)

// Sum of Positive and Negative Money Flow over the given length
Positive_Money_Flow_Sum = ta.sma(Positive_Money_Flow, length_MFI) * length_MFI
Negative_Money_Flow_Sum = ta.sma(Negative_Money_Flow, length_MFI) * length_MFI

// Calculate Money Flow Ratio
Money_Flow_Ratio = Positive_Money_Flow_Sum / Negative_Money_Flow_Sum

// Calculate MFI
MFI = 100 - (100 / (1 + Money_Flow_Ratio))

// Calculate MFI high and low bands
MFI_High = MFI - 80
MFI_Low = MFI - 20

// Plot the MFI
plot(MFI, color=color.blue, title="MFI")

// Plot the MFI high and low bands
hline(80, "MFI High", color=color.red, linestyle=hline.style_dashed)
hline(20, "MFI Low", color=color.green, linestyle=hline.style_dashed)
plot(MFI_High, color=color.red, title="MFI High Band")
plot(MFI_Low, color=color.green, title="MFI Low Band")


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
float op_operation = decision_tree_0_MSFT_1Hour_8078b50b(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, VIP, VIP_VIM, VIM)

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


