//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Stochastic_RSI
// ID_model: AVAXUSDT_1Hour_2CS0_931d83de Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_AVAXUSDT_1Hour_2CS0_931d83de", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_AVAXUSDT_1Hour_931d83de(ad, mf, ad_mf, rsi1, smoothK_k, d_k, k, d, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=6, max_features=0.9,min_samples_leaf=7, random_state=843828734)
	if( d_k <= 0.494218 )
		if( rsi1 <= 51.7366 )
			if( ad_mf <= -57077.5 )
				if( mf <= -0.050054 )
					if( d <= 5.47974 )
						if( d_k <= -0.254972 )
							ret := 0.155963
						if( d_k > -0.254972 )
							ret := -0.345679
					if( d > 5.47974 )
						if( k <= 64.2565 )
							ret := 0.581032
						if( k > 64.2565 )
							ret := 0.142857
				if( mf > -0.050054 )
					if( smoothK_k <= 43.8552 )
						if( mf <= 0.132822 )
							ret := 0.265152
						if( mf > 0.132822 )
							ret := -0.491803
					if( smoothK_k > 43.8552 )
						if( smoothK_k <= 56.0772 )
							ret := -0.568182
						if( smoothK_k > 56.0772 )
							ret := -0.092784
			if( ad_mf > -57077.5 )
				if( rsi1 <= 38.9565 )
					if( d_k <= -3.50866 )
						if( d <= 8.76349 )
							ret := 0.241470
						if( d > 8.76349 )
							ret := -0.111695
					if( d_k > -3.50866 )
						if( smoothK_k <= 15.5439 )
							ret := -0.190689
						if( smoothK_k > 15.5439 )
							ret := -0.411924
				if( rsi1 > 38.9565 )
					if( d_k <= -8.79585 )
						if( mf <= 0.007402 )
							ret := 0.272843
						if( mf > 0.007402 )
							ret := 0.010727
					if( d_k > -8.79585 )
						if( smoothD_d <= 16.8295 )
							ret := 0.137491
						if( smoothD_d > 16.8295 )
							ret := -0.073997
		if( rsi1 > 51.7366 )
			if( rsi1 <= 60.6776 )
				if( smoothD_d <= 30.5741 )
					if( mf <= 0.119229 )
						if( ad_mf <= 125814 )
							ret := 0.529904
						if( ad_mf > 125814 )
							ret := 0.093023
					if( mf > 0.119229 )
						if( rsi1 <= 59.096 )
							ret := 0.232639
						if( rsi1 > 59.096 )
							ret := 0.629032
				if( smoothD_d > 30.5741 )
					if( mf <= 0.065524 )
						if( smoothK_k <= 57.4536 )
							ret := 0.460587
						if( smoothK_k > 57.4536 )
							ret := 0.231010
					if( mf > 0.065524 )
						if( ad_mf <= 277178 )
							ret := 0.043779
						if( ad_mf > 277178 )
							ret := -0.515464
			if( rsi1 > 60.6776 )
				if( mf <= 0.201407 )
					if( smoothK_k <= 86.2541 )
						if( ad_mf <= -27212.4 )
							ret := 0.655527
						if( ad_mf > -27212.4 )
							ret := 0.481003
					if( smoothK_k > 86.2541 )
						if( rsi1 <= 69.4008 )
							ret := 0.269592
						if( rsi1 > 69.4008 )
							ret := 0.411652
				if( mf > 0.201407 )
					if( rsi1 <= 69.8943 )
						if( mf <= 0.328878 )
							ret := 0.066667
						if( mf > 0.328878 )
							ret := -0.543478
					if( rsi1 > 69.8943 )
						if( ad_mf <= 386614 )
							ret := 0.325203
						if( ad_mf > 386614 )
							ret := -0.078125
	if( d_k > 0.494218 )
		if( rsi1 <= 51.7592 )
			if( rsi1 <= 40.1412 )
				if( smoothD_d <= 38.0815 )
					if( rsi1 <= 31.1291 )
						if( ad_mf <= -436418 )
							ret := 0.478261
						if( ad_mf > -436418 )
							ret := -0.436017
					if( rsi1 > 31.1291 )
						if( mf <= -0.106507 )
							ret := -0.061511
						if( mf > -0.106507 )
							ret := -0.303689
				if( smoothD_d > 38.0815 )
					if( mf <= -0.250989 )
						if( smoothK_k <= 27.169 )
							ret := -0.727273 // sell
						if( smoothK_k > 27.169 )
							ret := 0.111111
					if( mf > -0.250989 )
						if( mf <= 0.124709 )
							ret := -0.553854
						if( mf > 0.124709 )
							ret := -0.186916
			if( rsi1 > 40.1412 )
				if( d_k <= 6.88848 )
					if( ad_mf <= -4471.71 )
						if( mf <= -0.111656 )
							ret := 0.241636
						if( mf > -0.111656 )
							ret := -0.027285
					if( ad_mf > -4471.71 )
						if( d_k <= 5.11117 )
							ret := -0.238132
						if( d_k > 5.11117 )
							ret := -0.451977
				if( d_k > 6.88848 )
					if( smoothD_d <= 35.296 )
						if( ad <= -75814.1 )
							ret := 0.124424
						if( ad > -75814.1 )
							ret := -0.245690
					if( smoothD_d > 35.296 )
						if( mf <= -0.051261 )
							ret := -0.170213
						if( mf > -0.051261 )
							ret := -0.454981
		if( rsi1 > 51.7592 )
			if( ad <= 54909.1 )
				if( d_k <= 4.14836 )
					if( ad_mf <= -710.6 )
						if( rsi1 <= 54.8219 )
							ret := 0.055970
						if( rsi1 > 54.8219 )
							ret := 0.330091
					if( ad_mf > -710.6 )
						if( ad_mf <= -0.229867 )
							ret := -0.863636 // sell
						if( ad_mf > -0.229867 )
							ret := 0.064669
				if( d_k > 4.14836 )
					if( d <= 82.2321 )
						if( d_k <= 11.6916 )
							ret := 0.156492
						if( d_k > 11.6916 )
							ret := -0.082432
					if( d > 82.2321 )
						if( d_k <= 4.45625 )
							ret := -0.576271
						if( d_k > 4.45625 )
							ret := -0.168531
			if( ad > 54909.1 )
				if( d <= 50.8925 )
					if( mf <= 0.147653 )
						if( ad <= 112138 )
							ret := -0.083333
						if( ad > 112138 )
							ret := 0.519608
					if( mf > 0.147653 )
						if( rsi1 <= 57.7983 )
							ret := -0.610526
						if( rsi1 > 57.7983 )
							ret := -0.139241
				if( d > 50.8925 )
					if( d_k <= 1.4564 )
						if( rsi1 <= 59.2861 )
							ret := -0.563636
						if( rsi1 > 59.2861 )
							ret := 0.227545
					if( d_k > 1.4564 )
						if( rsi1 <= 78.3902 )
							ret := -0.479440
						if( rsi1 > 78.3902 )
							ret := 0.000000
	
    ret //return
// Define expected timeframe based on the selected interval: 1Hour pine_value: 60   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1HOUR !!"
if (str.tostring(timeframe.period) != "60")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

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
float op_operation = decision_tree_0_AVAXUSDT_1Hour_931d83de(ad, mf, ad_mf, rsi1, smoothK_k, d_k, k, d, smoothD_d)

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


