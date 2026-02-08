//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Bull_Bear_Power, L_Chaikin_Money_Flow
// ID_model: BABA_1Hour_2BC0_72fd933a Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_BABA_1Hour_2BC0_72fd933a", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_BABA_1Hour_72fd933a(bullPower, bbp, bearPower, bbm, BBPower_Color, ad, mf, ad_mf)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( ad <= -163855 )
		if( bearPower <= -1.69181 )
			if( bbp <= -1.96152 )
				if( bearPower <= -9.34619 )
					if( bbp <= -16.175 )
						ret := -0.315789
					if( bbp > -16.175 )
						ret := -1.000000 // sell
				if( bearPower > -9.34619 )
					if( bullPower <= -2.80681 )
						if( ad_mf <= -873567 )
							ret := 0.148148
						if( ad_mf > -873567 )
							ret := 0.681818
					if( bullPower > -2.80681 )
						if( bbm <= 7.98179 )
							ret := 0.013514
						if( bbm > 7.98179 )
							ret := 0.700000 // buy
			if( bbp > -1.96152 )
				if( ad <= -5.40182e+06 )
					if( bbm <= 4.43446 )
						ret := 1.000000 // buy
					if( bbm > 4.43446 )
						ret := 0.090909
				if( ad > -5.40182e+06 )
					if( mf <= -0.332586 )
						if( bullPower <= 1.54426 )
							ret := -0.032258
						if( bullPower > 1.54426 )
							ret := 0.857143 // buy
					if( mf > -0.332586 )
						if( ad <= -3.05316e+06 )
							ret := 0.057971
						if( ad > -3.05316e+06 )
							ret := -0.371105
		if( bearPower > -1.69181 )
			if( bullPower <= 7.08439 )
				if( BBPower_Color <= 0.5 )
					if( bearPower <= -0.147936 )
						if( mf <= 0.186908 )
							ret := 0.092593
						if( mf > 0.186908 )
							ret := 0.447552
					if( bearPower > -0.147936 )
						if( ad_mf <= -522495 )
							ret := 0.537634
						if( ad_mf > -522495 )
							ret := -0.141509
				if( BBPower_Color > 0.5 )
					if( bullPower <= 1.99285 )
						if( bbm <= 2.48454 )
							ret := -0.002349
						if( bbm > 2.48454 )
							ret := -0.648649
					if( bullPower > 1.99285 )
						if( ad <= -5.79829e+06 )
							ret := -0.360656
						if( ad > -5.79829e+06 )
							ret := 0.182285
			if( bullPower > 7.08439 )
				if( bbp <= 13.4075 )
					ret := 1.000000 // buy
				if( bbp > 13.4075 )
					ret := 0.500000
	if( ad > -163855 )
		if( bbm <= 3.10653 )
			if( mf <= -0.140064 )
				if( bbm <= 0.223557 )
					if( bullPower <= -0.238048 )
						if( bbm <= 0.08867 )
							ret := -0.757143 // sell
						if( bbm > 0.08867 )
							ret := -0.274011
					if( bullPower > -0.238048 )
						if( bbp <= -0.420938 )
							ret := 0.144737
						if( bbp > -0.420938 )
							ret := -0.203704
				if( bbm > 0.223557 )
					if( ad_mf <= 4581.26 )
						if( ad <= 3885.07 )
							ret := -0.007361
						if( ad > 3885.07 )
							ret := 0.782609 // buy
					if( ad_mf > 4581.26 )
						if( ad_mf <= 4872.66 )
							ret := -0.925926 // sell
						if( ad_mf > 4872.66 )
							ret := -0.119261
			if( mf > -0.140064 )
				if( ad <= -36909.3 )
					if( mf <= 0.148064 )
						if( ad_mf <= -154184 )
							ret := -0.650000
						if( ad_mf > -154184 )
							ret := 0.001825
					if( mf > 0.148064 )
						if( ad <= -77397 )
							ret := -0.048128
						if( ad > -77397 )
							ret := -0.539474
				if( ad > -36909.3 )
					if( ad <= -34786.7 )
						if( mf <= 0.2675 )
							ret := 0.770000 // buy
						if( mf > 0.2675 )
							ret := 0.230769
					if( ad > -34786.7 )
						if( ad <= 7.54128e+06 )
							ret := 0.010838
						if( ad > 7.54128e+06 )
							ret := 0.888889 // buy
		if( bbm > 3.10653 )
			if( bearPower <= -1.7917 )
				if( mf <= 0.093863 )
					if( mf <= 0.064102 )
						if( mf <= -0.3542 )
							ret := 0.714286 // buy
						if( mf > -0.3542 )
							ret := -0.293629
					if( mf > 0.064102 )
						if( bbm <= 4.09702 )
							ret := 0.823529 // buy
						if( bbm > 4.09702 )
							ret := 0.000000
				if( mf > 0.093863 )
					if( bbm <= 4.05234 )
						if( ad <= 2.99311e+06 )
							ret := -0.058824
						if( ad > 2.99311e+06 )
							ret := -0.863636 // sell
					if( bbm > 4.05234 )
						if( bearPower <= -2.11436 )
							ret := -0.601942
						if( bearPower > -2.11436 )
							ret := -1.000000 // sell
			if( bearPower > -1.7917 )
				if( ad <= 7.35589e+06 )
					if( ad_mf <= -47720.7 )
						if( mf <= -0.056843 )
							ret := -0.428571
						if( mf > -0.056843 )
							ret := -0.878788 // sell
					if( ad_mf > -47720.7 )
						if( bbm <= 3.2604 )
							ret := -0.405405
						if( bbm > 3.2604 )
							ret := -0.002169
				if( ad > 7.35589e+06 )
					if( mf <= 0.218198 )
						ret := 0.523810
					if( mf > 0.218198 )
						if( bearPower <= 0.283917 )
							ret := 0.875000 // buy
						if( bearPower > 0.283917 )
							ret := 1.000000 // buy
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Bull_Bear_Power 
//@version=5
//indicator "Bull Bear Power", shorttitle="BBP")
lengthInput = input.int(13, title="Length")
bullPower = high - ta.ema(close, lengthInput)
bearPower = low - ta.ema(close, lengthInput)
bbp = bullPower + bearPower

bbm = bullPower - bearPower

plot(bbp, color = bbp >= 0 ? #089981 : #f23645, title="BBPower", style = plot.style_columns)
hline(0, "Zero line")

BBPower_Color = bbp >= 0  ? 1: 0


//CODE associated with the technical indicator L_Chaikin_Money_Flow 
 //@version=5
//indicator title="Chaikin Money Flow", shorttitle="CMF", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
var cumVol = 0.
cumVol += nz(volume)
if barstate.islast and cumVol == 0
    runtime.error("No volume is provided by the data vendor.")
length_CMF = input.int(20, minval=1)
ad = close==high and close==low or high==low ? 0 : ((2*close-low-high)/(high-low))*volume
mf = math.sum(ad, length_CMF) / math.sum(volume, length_CMF)
plot(mf, color=#43A047, title="MF")
hline(0, color=#787B86, title="Zero", linestyle=hline.style_dashed)


ad_mf = ad - mf
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
float op_operation = decision_tree_0_BABA_1Hour_72fd933a(bullPower, bbp, bearPower, bbm, BBPower_Color, ad, mf, ad_mf)

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


