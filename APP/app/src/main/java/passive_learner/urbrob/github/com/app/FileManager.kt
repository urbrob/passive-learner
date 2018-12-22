package passive_learner.urbrob.github.com.app

import android.content.Context
import java.io.File
import java.io.FileInputStream

class FileManager(context: MainActivity) {
    private val ctx: MainActivity = context

    private fun copyToLocal(fileName: String, source: File) {
        source.inputStream().use { input ->
            ctx.openFileOutput(fileName, Context.MODE_PRIVATE).use { output ->
                input.copyTo(output)
            }
        }
    }

    fun saveToLocalFile(fileName: String, content: String) {
        ctx.openFileOutput(fileName, Context.MODE_PRIVATE).use {
            it.write(content.toByteArray())
        }
    }

    fun deleteLocalFile(fileName: String) {
        ctx.deleteFile(fileName)
    }

    fun setActualPlan(fileName: String): FileInputStream {
        val pref = ctx.getPreferences(Context.MODE_PRIVATE)
        with(pref.edit()) {
            putString("actualPlan", fileName)
            apply()
        }
        return ctx.openFileInput(fileName)
    }

    fun getActualPlan(): FileInputStream {
        val fname = ctx.getPreferences(Context.MODE_PRIVATE).getString("actualPlan", null)
        return ctx.openFileInput(fname)
    }

    fun importExternalFile(path: String, newFileName: String? = null, makeActual: Boolean = false): FileInputStream? {
        val fname: String
        val file = File(path)
        fname = if (newFileName.isNullOrBlank()) {
            file.name
        } else {
            newFileName
        }
        copyToLocal(fname, file)
        if (makeActual) {
            return setActualPlan(fname)
        }
        return null
    }
}