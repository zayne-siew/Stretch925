import styles from '@/styles/BreakTime.module.css'


const BreakTime = ({
    numSessions,
    breakSecondsLeft,
    initStretch
}) => {
    return (
        <>
            <p>Number of sessions left: {numSessions}</p>
            <p className={styles.breakTimer}>Break time left: {Math.floor(breakSecondsLeft/60)}:{(breakSecondsLeft - (Math.floor(breakSecondsLeft/60) * 60) < 10) ? 0:<></>}{breakSecondsLeft - (Math.floor(breakSecondsLeft/60) * 60)}</p>

            <h1 className={styles.header}>BREAK<br/>TIME</h1>
            <button className={styles.stretchButton} onClick={() => initStretch()}>STRETCH!!!</button>
            
        </>
    );
}

export default BreakTime;