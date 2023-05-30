import styles from '@/styles/Pomodoro.module.css'

const Pomodoro = ({
    isTimerActive, 
    setIsTimerActive, 
    secondsLeft, 
    setSecondsLeft, 
    startTimer, 
    stopTimer,
    numSessions,
    skipTimer
}) => {
    return ( 
        <>
        <p>Number of sessions left: {numSessions}</p>
         <div className={styles.timer}>
            <h1>{Math.floor(secondsLeft/60)}:{(secondsLeft - (Math.floor(secondsLeft/60) * 60) < 10) ? 0:<></>}{secondsLeft - (Math.floor(secondsLeft/60) * 60)}</h1>
        </div>

        {
            (!isTimerActive) ? 
            <button className={styles.startButton} onClick={() => startTimer()}>START</button> :
            <div className={styles.stopSkipContainer}>
                <button className={styles.skipButton} onClick={() => skipTimer("normal")}>SKIP</button>
                <button className={styles.stopButton} onClick={() => stopTimer()}>END</button>
            </div>
            
        }
        
        {(!isTimerActive) ? <button className={styles.editButton}>Edit Sessions</button> : <></>}
        
        </>
       
     );
}
 
export default Pomodoro;